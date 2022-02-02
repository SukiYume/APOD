import subprocess, datetime

def git_push():
    p = subprocess.Popen('python status.py', shell=True, 
                 stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    _ = p.wait()
    print(1)
    p = subprocess.Popen('git add .', shell=True, 
                 stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    _ = p.wait()
    print(2)
    today_date = datetime.datetime.today().strftime('%Y-%m-%d')
    commit_content = 'git commit -m "{}"'.format(today_date)
    p = subprocess.Popen(commit_content, shell=True, 
                     stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    _ = p.wait()
    print(3)
    p = subprocess.Popen('git push', shell=True, 
                     stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out, _  = p.communicate()
    _ = p.wait()
    return out

if __name__ == '__main__':
    print(git_push())