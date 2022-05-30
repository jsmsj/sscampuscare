import discord
import aiosqlite
import requests

from pathlib import Path


def get_path():
    """
    A function to get the current path to bot.py
    Returns:
     - cwd (string) : Path to bot.py directory
    """
    cwd = Path(__file__).parents[1]
    cwd = str(cwd)
    return cwd

def image_exists(path):
    x = requests.get(path)
    return x.status_code != 404

def get_user_data(userid:str):
    url = "https://www.sscampuscare.in/Logon/UserConfirm"
    data = {"Userid":userid}
    x = requests.post(url, data = data).json()
    try:
        return x["Data"][0][0]
    except:
        return False

def make_data_tuple(data:dict):
    return (data["UserName"], data["UserID"],data["EmployeeIDStudentID"], data["UID"],data["UserTypeID"])

def give_help(stuff):
    if stuff == "search":
        em = discord.Embed(title="Hi",color=discord.Color.green())
        return em

async def search_online_student_details(ls):
    em = discord.Embed(description="Admission Number Not Found",color=discord.Color.green())
    adnum = ls[1]
    dataa = get_user_data("s"+str(adnum))
    if dataa:
        data = make_data_tuple(dataa)
        em = discord.Embed(title=data[0],color=discord.Color.green())
        em.add_field(name="Admission Number",value=f"```yaml\n{data[1][1:]}\n```")
        em.add_field(name="Employee Student ID",value=f"```yaml\n{data[2]}\n```")
        em.add_field(name="UID",value=f"```yaml\n{data[3]}\n```",inline=False)
        em.add_field(name="Type",value="```yaml\nStudent\n```")
        em.set_footer(text="Powered by sscampuscare :)")
        if image_exists(f"https://www.sscampuscare.in/StudentPhoto/S{dataa['EmployeeIDStudentID']}.jpg"):
            url = url=f"https://www.sscampuscare.in/StudentPhoto/S{dataa['EmployeeIDStudentID']}.jpg"
        else:
            url="https://www.sscampuscare.in/StudentPhoto/noImage.png"
        return [em,url]
    return [em]

async def search_online_parent_details(ls):
    em = discord.Embed(description="Admission Number Not Found",color=discord.Color.green())
    adnum = ls[1]
    dataa = get_user_data("p"+str(adnum))
    if dataa:
        data = make_data_tuple(dataa)
        em = discord.Embed(title=data[0],color=discord.Color.green())
        em.add_field(name="Admission Number of Child",value=f"```yaml\n{data[1][1:]}\n```")
        em.add_field(name="Employee Student ID",value=f"```yaml\n{data[2]}\n```")
        em.add_field(name="UID",value=f"```yaml\n{data[3]}\n```",inline=False)
        em.add_field(name="Type",value="```yaml\nParent\n```")
        em.set_footer(text="Powered by sscampuscare :)")
        if image_exists(f"https://www.sscampuscare.in/FatherPhoto/F{dataa['EmployeeIDStudentID']}.jpg"):
            url = f"https://www.sscampuscare.in/FatherPhoto/F{dataa['EmployeeIDStudentID']}.jpg"
        else:
            url="https://www.sscampuscare.in/StudentPhoto/noImage.png"
        return [em,url]
    return [em]

async def give_details_from_admn(ls):
    em = discord.Embed(description="Admission Number Not Found",color=discord.Color.green())
    file = discord.File(r"./userdata/images/image.png")
    check = em
    if len(ls) == 0: return em
    db = await aiosqlite.connect(r"./userdata/data.db")
    if not ls[0] or ls[0].lower() =="s":
        cursor = await db.execute(f'SELECT * FROM students WHERE userid="S{ls[1]}" and usertype=2')
        data = await cursor.fetchone()
        if data:
            em = discord.Embed(title=data[0],color=discord.Color.green())
            em.add_field(name="Admission Number",value=f"```yaml\n{data[1][1:]}\n```")
            em.add_field(name="Employee Student ID",value=f"```yaml\n{data[2]}\n```")
            em.add_field(name="UID",value=f"```yaml\n{data[3]}\n```",inline=False)
            em.add_field(name="Type",value="```yaml\nStudent\n```")
            em.set_footer(text="Powered by sscampuscare :)")
            try:
                file = discord.File(get_path() + f"\\userdata\\images\\{data[2]}.jpg",filename="temp.jpg")
                em.set_image(url=f"attachment://temp.jpg")
            except:
                file = discord.File(get_path() + "\\userdata\\images\\image.png",filename="image.png")
                em.set_image(url="attachment://image.png")
        if em == check:
            temp = await search_online_student_details(ls)
            em = temp[0]
            try:
                em.set_image(url=temp[1])
            except:pass    
            file=None
    else:
        cursor = await db.execute(f'SELECT * FROM parents WHERE userid="P{ls[1]}" and usertype=3')
        data = await cursor.fetchone()
        if data:
            em = discord.Embed(title=data[0],color=discord.Color.green())
            em.add_field(name="Admission Number of Child",value=f"```yaml\n{data[1][1:]}\n```",inline=False)
            em.add_field(name="Employee Student ID",value=f"```yaml\n{data[2]}\n```")
            em.add_field(name="UID",value=f"```yaml\n{data[3]}\n```")
            em.add_field(name="Type",value="```yaml\nParent\n```",inline=False)
            em.set_footer(text="Powered by sscampuscare :)")
            try:
                file = discord.File(get_path() + f"\\userdata\\pimages\\{data[2]}.jpg",filename="temp.jpg")
                em.set_image(url=f"attachment://temp.jpg")
            except:
                file = discord.File(get_path() + "\\userdata\\pimages\\image.png",filename="image.png")
                em.set_image(url="attachment://image.png")
        if em == check:
            temp = await search_online_parent_details(ls)
            em = temp[0]
            try:
                em.set_image(url=temp[1])
            except:pass    
            file=None

    return [file,em]

