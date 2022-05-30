#  if (UserTypeid == '0') {
#                         if (imageExists("/EmployeePhotos/E" + EmpStudID + ".jpg") == true) {
#                             document.getElementById('UserImg').src = '../EmployeePhotos/E' + EmpStudID + '.jpg?varDate=?varDate=' + varDate + '&TypeID=ImgePath"';
#                         }
#                         else {
#                             document.getElementById('UserImg').src = "/EmployeePhotos/noImage.png";
#                         }
#                         $('#UserTypeDetails').html('Admin');
#                         $('#cbp-spmenu-s2').show();
#                         $('#SecondMenu').hide();
#                         document.getElementById('wlportalname').style.display = ""
#                         document.getElementById('wlportalname1').style.display = ""
#                         //document.getElementById('wl').style.display = "none";
#                         document.getElementById('fResetPassword').style.display = "none";

#                     }
#                     if (UserTypeid == '1') {
#                         if (imageExists("/EmployeePhotos/E" + EmpStudID + ".jpg") == true) {
#                             document.getElementById('UserImg').src = '../EmployeePhotos/E' + EmpStudID + '.jpg?varDate=?varDate=' + varDate + '&TypeID=ImgePath"';
#                         }
#                         else {
#                             document.getElementById('UserImg').src = "/EmployeePhotos/noImage.png";
#                         }

#                         $('#UserTypeDetails').html('Staff');
#                         $('#cbp-spmenu-s2').show();
#                         $('#SecondMenu').hide();
#                         document.getElementById('wlportalname').style.display = ""
#                         document.getElementById('wlportalname1').style.display = ""
#                         //document.getElementById('wl').style.display = "none"
#                         document.getElementById('fResetPassword').style.display = "none";
#                     }
#                     else if (UserTypeid == '2') {
#                         if (imageExists("../StudentPhoto/S" + EmpStudID + ".jpg") == true) {
#                             document.getElementById('UserImg').src = '../StudentPhoto/S' + EmpStudID + '.jpg?varDate=?varDate=' + varDate + '&TypeID=ImgePath"';
#                         }
#                         else {
#                             document.getElementById('UserImg').src = "../StudentPhoto/noImage.png";
#                         }
#                         $('#cbp-spmenu-s2').show();
#                         $('#SecondMenu').hide();
#                         $('#UserTypeDetails').html('Student');
#                         document.getElementById('wlportalname').style.display = ""
#                         document.getElementById('wlportalname1').style.display = ""
#                         //document.getElementById('wl').style.display = "none"
#                         document.getElementById('fResetPassword').style.display = "";
#                     }
#                     else if (UserTypeid == '3') {
#                         if (imageExists("../FatherPhoto/F" + EmpStudID + ".jpg") == true) {
#                             document.getElementById('UserImg').src = '../FatherPhoto/F' + EmpStudID + '.jpg?varDate=?varDate=' + varDate + '&TypeID=ImgePath"';
#                         }
#                         else {
#                             document.getElementById('UserImg').src = "../FatherPhoto/noImage.png";
#                         }
#                         $('#cbp-spmenu-s2').show();
#                         $('#SecondMenu').hide();
#                         $('#UserTypeDetails').html('Parent');
#                         document.getElementById('wlportalname').style.display = ""
#                         document.getElementById('wlportalname1').style.display = ""
#                         //document.getElementById('wl').style.display = "none"
#                         document.getElementById('fResetPassword').style.display = "";
#                     }
#                     else if (UserTypeid == '4') {
#                         if (imageExists("../StudentPhoto/S" + EmpStudID + ".jpg") == true) {
#                             document.getElementById('UserImg').src = '../StudentPhoto/S' + EmpStudID + '.jpg?varDate=?varDate=' + varDate + '&TypeID=ImgePath"';
#                         }
#                         else {
#                             document.getElementById('UserImg').src = "../StudentPhoto/noImage.png";
#                         }
#                         $('#cbp-spmenu-s2').show();
#                         $('#SecondMenu').hide();
#                         $('#UserTypeDetails').html('Staff');
#                         document.getElementById('wlportalname').style.display = ""
#                         document.getElementById('wlportalname1').style.display = ""
#                         //document.getElementById('wl').style.display = "none"
#                         document.getElementById('fResetPassword').style.display = "none";
#                     } else if (UserTypeid == '6') {
#                         if (imageExists("../StudentPhoto/SR" + EmpStudID + ".jpg") == true) {
#                             document.getElementById('UserImg').src = '../StudentPhoto/SR' + EmpStudID + '.jpg?varDate=?varDate=' + varDate + '&TypeID=ImgePath"';
#                         }
#                         else {
#                             document.getElementById('UserImg').src = "../StudentPhoto/noImage.png";
#                         }
#                         $('#cbp-spmenu-s2').show();
#                         $('#SecondMenu').hide();
#                         $('#UserTypeDetails').html('Registration');
#                         document.getElementById('wlportalname').style.display = ""
#                         document.getElementById('wlportalname1').style.display = ""
#                         //document.getElementById('wl').style.display = "none"
#                         document.getElementById('fResetPassword').style.display = "";
#                     }
#                     else if (UserTypeid == '7') {
#                         if (imageExists("/EmployeePhotos/E" + EmpStudID + ".jpg") == true) {
#                             document.getElementById('UserImg').src = '../EmployeePhotos/E' + EmpStudID + '.jpg?varDate=?varDate=' + varDate + '&TypeID=ImgePath"';
#                         }
#                         else {
#                             document.getElementById('UserImg').src = "/EmployeePhotos/noImage.png";
#                         }
#                         $('#UserTypeDetails').html('Principal');
#                         $('#cbp-spmenu-s2').show();
#                         $('#SecondMenu').hide();
#                         document.getElementById('wlportalname').style.display = ""
#                         document.getElementById('wlportalname1').style.display = ""
#                         //document.getElementById('wl').style.display = "none"
#                         document.getElementById('fResetPassword').style.display = "none";
#                     } if (UserTypeid == '8') {
#                         if (imageExists("/EmployeePhotos/E" + EmpStudID + ".jpg") == true) {
#                             document.getElementById('UserImg').src = '../EmployeePhotos/E' + EmpStudID + '.jpg?varDate=?varDate=' + varDate + '&TypeID=ImgePath"';
#                         }
#                         else {
#                             document.getElementById('UserImg').src = "/EmployeePhotos/noImage.png";
#                         }
#                         $('#UserTypeDetails').html('HOD');
#                         $('#cbp-spmenu-s2').show();
#                         $('#SecondMenu').hide();
#                         document.getElementById('wlportalname').style.display = ""
#                         document.getElementById('wlportalname1').style.display = ""
#                         //document.getElementById('wl').style.display = "none"
#                         document.getElementById('fResetPassword').style.display = "none";
#                     }
#                     $("#password").focus();
#                     $('#sp_error1').html('');
#                 }

import helpers as hp
import sqlite3,time
import sys

db = sqlite3.connect('./userdata/data.db')
hp.connect_db(db)

og_std = sys.stdout

def students_records():
    start = time.time()
    records = 9999
    for i in range(9150,records+1):
        s = time.time()
        data = hp.get_user_data(f"s{str(i).zfill(4)}")
        if data:
            hp.update_db(db,hp.make_data_tuple(data))
            hp.download_image(f"https://www.sscampuscare.in/StudentPhoto/S{data['EmployeeIDStudentID']}.jpg", data['EmployeeIDStudentID'],"student")
            val = "yes"
        else:
            val = "no"
        e = time.time()
        with open("./std.txt","a") as f:
            sys.stdout = f
            print(f"{i} -- {e-s}s -- {val}")
            sys.stdout = og_std
        print(f"{i} -- {e-s}s -- {val}")

    end = time.time()


    print(f"Total time taken : {end-start}\n Average time : {(end-start)/records}")

def parents_records():
    start = time.time()
    records = 9150
    for i in range(2000,records+1):
        s = time.time()
        data = hp.get_user_data(f"p{str(i).zfill(4)}")
        if data:
            hp.update_db_parents(db,hp.make_data_tuple(data))
            hp.download_image(f"https://www.sscampuscare.in/FatherPhoto/F{data['EmployeeIDStudentID']}.jpg", data['EmployeeIDStudentID'],"parent")
            val = "yes"
        else:
            val = "no"
        e = time.time()
        with open("./std.txt","a") as f:
            sys.stdout = f
            print(f"{i} -- {e-s}s -- {val}")
            sys.stdout = og_std
        print(f"{i} -- {e-s}s -- {val}")

    end = time.time()
    print(f"Total time taken : {end-start}\n Average time : {(end-start)/records}")


parents_records()