import os, webbrowser, time, threading

title_text = '''博客快捷指令：
new: 按照提示，新建博客文章
ed, edit: 打开 _post 目录，编辑文件
gd: 生成并部署博客
all: 生成博客，部署，并运行本地服务器，预览博客
s, server: 运行本地服务器，预览博客
g, generate: 生成博客
d, deploy: 部署博客
c, clean: 清理博客文件
cmd: 进入命令行
e, exit: 退出程序
'''
prompt_sign = ">> "
cwd = os.getcwd()


# 新建文章
def new_passage():
    psg_layout = input("请输入文章布局（默认为 post）：")
    if psg_layout == "":
        psg_layout = "post"
    psg_title = input("请输入文章标题：")
    psg_slug = input("请输入浏览器地址名：")
    hexo_command = 'hexo new ' + psg_layout + ' \"' + psg_title + '\" -s \"' + psg_slug + '\"'
    os.system(hexo_command)
    os.startfile(cwd + r"\source\_posts")
    print("成功新建文章")

def generate():
    os.system("hexo g")
    print("博客已生成")

def deploy():
    os.system("hexo d")
    print("博客已部署")

def open_webbrowser():
    time.sleep(1.3) # in second
    webbrowser.open("http://localhost:4000/")

def server():
    x = threading.Thread(target = open_webbrowser, args = ())
    try:
        x.start()
        os.system("hexo s")
    except KeyboardInterrupt:
        print("预览结束")
    finally:
        x.join()

def generate_deploy():
    generate()
    deploy()

def all_action():
    generate()
    deploy()
    server()

def clean():
    os.system("hexo clean")
    print("已清理博客文件")

def run_cmd():
    try:
        os.system("cmd")
    except KeyboardInterrupt:
        pass
    print("已退出命令行")

def main():
    print(title_text)
    is_running = True
    print("当前工作目录：" + cwd + "\n")
    while is_running:
        command = input(prompt_sign)
        if command == "new":
            new_passage()
        elif command in ("ed", "edit"):
            os.startfile(cwd + r"\source\_posts")
            print("成功打开文章编辑目录")
        elif command == "gd":
            generate_deploy()
        elif command == "all":
            all_action()
        elif command in ("s", "server"):
            server()
        elif command in ("g", "generate"):
            generate()
        elif command in ("d", "deploy"):
            deploy()
        elif command in ("c", "clean"):
            clean()
        elif command == "cmd":
            run_cmd()
        elif command in ("e", "exit"):
            is_running = False

if __name__ == "__main__":
    main()