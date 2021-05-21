def compressFolder(folderPath, compressPathName):
    '''
    :param folderPath: 文件夹路径
    :param compressPathName: 压缩包路径
    :return:

    e.g.: compressFolder('/content/cloned-repo/results/fMRI/test_latest/images', '/content/cloned-repo/results/fMRI/test_latest/result.zip')
    '''
    import zipfile
    zip = zipfile.ZipFile(compressPathName, 'w', zipfile.ZIP_DEFLATED)
    dict = {}
    
    for path, dirNames, fileNames in os.walk(folderPath):
        fpath = path.replace(folderPath, '')
        for name in fileNames:
            fullName = os.path.join(path, name)#.decode(encoding='gbk')
            
            name = fpath + '\\' + name
            zip.write(fullName, name)

    zip.close()