def print_directory_contents(sPath):
    """
    """
    import os
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath, sChild)
        if os.path.isdir(sChildPath):
            print('is Dir:', sChildPath)
            print_directory_contents(sChildPath)
        else:
            print('is File', sChildPath)

if __name__ == '__main__':
    # print_directory_contents('/tmp')
    print_directory_contents('/Users/huoyinghui/github/docker_elk')
