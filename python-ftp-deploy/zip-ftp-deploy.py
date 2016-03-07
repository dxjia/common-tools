#encoding: utf-8
__author__ = 'dxjia'
__mail__ = 'jdxwind@dxjia.cn'
__date__ = '2016-03-07'
__version = 1.0

import os, os.path
import zipfile
from ftplib import FTP

#全局变量
PUBLIC_FOLDER_NAME = 'public'
#目标压缩包文件名
TARGET_ZIP_FILE_NAME = 'a-ftp-deplog.zip'
#FTP参数
FTP_IP = "网站FTP IP地址"
FTP_USER_NAME = '用户名'
FTP_PASSWORD = '密码'
FTP_TARGET_FOLDER = 'htdocs' #网站目录

#打包函数
def zip_dir(dirname, zipfilename):
    filelist = []
    if os.path.isfile(dirname):
        filelist.append(dirname)
    else :
        for root, dirs, files in os.walk(dirname):
            for name in files:
                filelist.append(os.path.join(root, name))
         
    zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)
    for tar in filelist:
        arcname = tar[len(dirname):]
        zf.write(tar,arcname)
    zf.close()
 
if __name__ == '__main__':
    public_path = os.path.join(os.getcwd(), PUBLIC_FOLDER_NAME)
    zip_file_path = os.path.join(os.getcwd(), TARGET_ZIP_FILE_NAME)
    if os.path.exists(public_path):
        zip_dir(public_path, zip_file_path)
    else:
        print "have no public folder, please excute \'hexo g\' first"

    if os.path.exists(zip_file_path):
        ftp = FTP(FTP_IP)
        ftp.login(FTP_USER_NAME, FTP_PASSWORD)
        ftp.cwd(FTP_TARGET_FOLDER)
        f = open(zip_file_path, 'rb')
        ftp.storbinary('STOR %s' % TARGET_ZIP_FILE_NAME, f)
        f.close()
        ftp.close()
    else:
        print "failed"