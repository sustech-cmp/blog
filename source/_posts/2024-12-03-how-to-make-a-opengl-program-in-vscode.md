---
title: 如何在 VS Code 上创建自己的第一个 OpenGL 窗口
date: 2024-12-03 21:46:52
category: 计算机图形学
tags:
- OpenGL
- 图形编程
---

这篇文章介绍如何在 VS Code 上配置 OpenGL 环境，并运行自己的第一个图形窗口。

> 系统环境：Windows 11 (64 位)，软件环境：VS Code，使用 g++ 编译。

<!--more-->

# 我参考的教程资料

一、VS Code 上面如何配置 Build Tasks：[YouTube 快速教程](https://www.youtube.com/watch?v=QNFGtTbTH-A&ab_channel=VisualStudioCode)。Build Tasks 可以用来管理项目文件。

二、LearnOpenGL 网站上的配置教程（比较冗长）：[链接](https://learnopengl.com/Getting-started/Creating-a-window)，[中文翻译版本](https://learnopengl-cn.github.io/01%20Getting%20started/02%20Creating%20a%20window/)；

文章中会用到的 [创建第一个窗口的代码](https://learnopengl.com/Getting-started/Hello-Window)。

三、OpenGL 的“Window Toolkits”都有哪些：[官方文档](https://www.khronos.org/opengl/wiki/Related_toolkits_and_APIs#Context/Window_Toolkits)。

四、出现“undefined reference to \`CreateDCW@16'”错误的解决方法：[StackOverflow 链接](https://stackoverflow.com/questions/22008845/glfw-mingw-link-error)。（解决方案：加入 `-lgdi32`）

# 目录

- 关于 `g++` 的配置问题，确认配置正确。
- 如何下载 OpenGL 相关的各种文件：GLFW / freeglut / GLAD 的头文件（`.h`）和库文件（`.o`），GLAD 的 `glad.c` 文件。
- 如何配置 `include` 和 `lib` 目录。
- 如何在 VS Code 里创建 Build Tasks 配置文件。
- Build Tasks 文件应该怎么写。
- 编译自己的第一个窗口程序。

# 一、关于 g++ 的配置问题

我使用的是 msys64 下面的 mingw64。

假如 msys64 的软件根目录为 `D:\Software\msys64\`，那么我使用的 `g++.exe` 位于 `D:\Software\msys64\mingw64\bin` 下面。

为了让 VS Code 找到 `g++.exe`，需要配置 Path 环境变量。在 Windows 的环境变量设置里面，加入 `D:\Software\msys64\mingw64\bin` 即可。

# 二、下载 OpenGL 相关的各种文件

需要下载的文件有：

1. freeglut，内含一个文件夹 `GL`，下面有 5 个 `.h` 文件：

```
GL\freeglut.h
GL\freeglut_ext.h
GL\freeglut_std.h
GL\freeglut_ucall.h
GL\glut.h
```

freeglut 从这里下载：[链接](https://freeglut.sourceforge.net/)，在 Stable Releases 栏目下面，找到最新版本下载即可。

解压压缩包，将会在 `include` 文件夹下面找到这个 `GL` 文件夹。**将来这个 GL 文件夹将会被整个地放入 g++ 的 include 目录里面。**详见第三部分。

2. GLFW，内含一个文件夹 `GLFW`（包含 `.h` 文件）和一个文件夹 `lib-mingw-w64`（包含 `.dll` 和 `.a` 库文件）。

`GLFW` 文件夹下面有：

```
GLFW\glfw3.h
GLFW\glfw3native.h
```

`lib-mingw-w64` 文件夹下面有：

```
lib-mingw-w64\glfw3.dll
lib-mingw-w64\libglfw3.a
lib-mingw-w64\libglfw3dll.a
```

GLFW 从这里下载：[链接](https://www.glfw.org/download.html)，在 Windows pre-compiled binaries 栏目下面，找到 64-bit Windows binaries。

解压压缩包之后，找到 `include` 文件夹里面的 `GLFW`。**将来这个 GLFW 文件夹将会被整个地放入 include 目录里面。**

再找到 `lib-mingw-w64`。**将来这个 .dll 文件和两个 .a 文件将会放到 lib 目录里面。**详见第三部分。

3. GLAD，在[这个教程](https://learnopengl.com/Getting-started/Creating-a-window)这里找到下载的方法。

![image-20241203223646282](image-20241203223646282.png)

注意上面的这些要求。下面展示应该怎么填：

![image-20241203223942014](image-20241203223942014.png)

点击 Generate 生成一个压缩包。

![image-20241203224009402](image-20241203224009402.png)

压缩包里面有一个 `include` 文件夹和一个 `src` 文件夹。**将来 include 文件夹里的东西要放入 g++ 的 include 目录中，src 文件夹里面的 glad.c 将会作为项目的一部分进行编译。**

# 三、如何配置 include 和 lib 目录

我在 D 盘下创建了一个自己的文件夹 `D:\myprograms\cpp`，下面包括：

```
D:\myprograms\cpp\include\
D:\myprograms\cpp\lib\
```

以后，就可以将自己需要的第三方库文件放到这里面。

现在，把这两个目录分别加入环境变量 CPLUS_INCLUDE_PATH 和 LIBRARY_PATH 中：

![image-20241203224613420](image-20241203224613420.png)

之后，每次调用 `g++ myfile.cpp -o myfile.exe` 的时候，就会自动把这两个文件夹作为 include 目录和 lib 目录了。

**接下来把刚刚下载的文件放进去**。

![image-20241203224754372](image-20241203224754372.png)

![image-20241203224818208](image-20241203224818208.png)

如上图所示。文件就配置好了。

# 四、如何创建 VS Code 的 Build Tasks 文件

VS Code 官方在 YouTube 上提供了一个创建 Build Tasks 的教程：[视频链接](https://www.youtube.com/watch?v=QNFGtTbTH-A&ab_channel=VisualStudioCode)。下面我也会给出教程。

首先在 VS Code 中打开一个文件夹。我这里是 simplefunc 这个文件夹。创建一个 `.cpp` 文件之后，选择“Terminal -> Configure Default Build Task...”：

![f5c02ad88974f37f77b38aff795078a1](f5c02ad88974f37f77b38aff795078a1.png)

将会弹出如下界面：

![image-20241203225532092](image-20241203225532092.png)

此时，选择 C/C++: g++.exe build active file 这个选项。由于我已经将 `D:\Software\msys64\mingw64\bin\` 加入到 Path 环境变量中，所以 VS Code 自动找到了 `g++.exe`。点击选项之后，VS Code 将会自动生成一份 `tasks.json` 文件：

![image-20241203225823307](image-20241203225823307.png)

这就是我们想要的配置文件了。

# 五、怎么配置需要的编译命令

这里给出我的 `tasks.json` 配置，注释里逐一写出了各个参数的含义。

```json
// .vscode\tasks.json
{
    "version": "2.0.0",
    "tasks": [
        {
            "type": "cppbuild",
            "label": "C/C++: g++.exe build project with OpenGL", // The name of this build task
            "command": "D:\\Software\\msys64\\mingw64\\bin\\g++.exe", // Using g++.exe as the compiler
            "args": [
                "-fdiagnostics-color=always", // Enable colorful diagnostics for compiler warning/error messages
                "-Wall", // Output warnings as much as possible
                "-std=c++11", // Using C++ 11 language standard
                "-g", // Enable debugging flag
                "${file}", // The filename of .cpp file
                "glad.c", // Compiling glad.c together with the .cpp file in the project
                "-o", // Output executable file
                "${fileDirname}\\..\\bin\\${fileBasenameNoExtension}.exe", // If .cpp files are in D:\projects\simplefunc\src folder, then the output .exe file will be in D:\projects\simplefunc\bin folder.
                // The following arguments are needed for the OpenGL library
                "-lfreeglut",
                "-lopengl32",
                "-lglu32",
                "-lglew32",
                "-lglfw3",
                "-lgdi32",
            ],
            "options": {
                "cwd": "${fileDirname}"
            },
            "problemMatcher": [
                "$gcc"
            ],
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "detail": "compiler: D:\\Software\\msys64\\mingw64\\bin\\g++.exe"
        }
    ]
}
```

注意如果出现以下报错，有可能是因为没有添加 `"-lgdi32"` 参数：

```
ld.exe: ...... win32_monitor.:(.text+0x11f): undefined reference to `__imp_CreateDCW'
ld.exe: ...... win32_monitor.:(.text+0x15e): undefined reference to `__imp_GetDeviceCaps'
ld.exe: ...... win32_monitor.:(.text+0x1b4): undefined reference to `__imp_DeleteDC'
ld.exe: ...... win32_monitor.:(.text+0x30b): undefined reference to `__imp_GetDeviceCaps'
ld.exe: ...... win32_monitor.:(.text+0x95b): undefined reference to `__imp_GetDeviceCaps'
ld.exe: ...... win32_monitor.:(.text+0xaeb): undefined reference to `__imp_GetDeviceCaps'
.........................
```

# 六、编译自己的第一个窗口程序

把[“Hello Window”教程](https://learnopengl.com/Getting-started/Hello-Window)最后的这段[程序](https://learnopengl.com/code_viewer_gh.php?code=src/1.getting_started/1.2.hello_window_clear/hello_window_clear.cpp)复制到项目目录下的 `main.cpp` 里面。

按 Ctrl + Shift + P 调出命令面板，输入 Tasks: Run Build Task 编译，就可以编译出程序文件啦！

点击程序，就可以看到一个绿色的小窗口。大功告成！

![image-20241203234820460](image-20241203234820460.png)
