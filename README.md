# CS61A-Fall-2020
My solutions and experience for CS61A Fall 2020.

## 一、课程介绍

这门课作为Berkeley大一新生的第一门计算机课程，是一门计算机导论的课程，主要的编程语言是python，此外还介绍了LISP的方言Scheme语法和SQL的基础用法。其核心思想是abstraction, 此外还讲了高阶函数，递归，OOP，函数式编程的思想和应用。总的来说涉猎比较广，但毕竟还是导论性质的课，许多地方并没有深挖。

## 二、为什么选择CS61A？

笔者起初是受到github上flyingpig的[csdiy.wiki](http://csdiy.wiki/)的影响，加之寒假也想自学python语言，进而选择了CS61A这门课程。这门课程有着相当多的优点：

1. 课程设计。国外优质的网课一般都有自己的网站，这门课也是如此。在笔者第一次进入网站时，就被眼花缭乱的资源震撼，有playlist, lecture, lab, discussion, homework, project, Q&A等等让你从学习知识到真正掌握知识。而且四个project中前三个都是做游戏，且为你写好了gui的图形化界面，在你每完成一个部分之后就可以打开游戏体验自己的成果，非常有成就感。

   <img src="D:\User\桌面\CS61A Fall 2020.jpeg" alt="CS61A Fall 2020" style="zoom:50%;" />

2. 课程的reading部分是经典教材***Structure and Interpretation of Computer Programs***，由John DeNero改编为[基于Python语言的SICP](http://composingprograms.com/)

3. 采用ok本地测试。一般国外课程都会有gradescope来在线评测你的答案，这也导致许多优质的课程我们做了作业后并不能得到有效的反馈。但61A开发了一个ok的评测系统，对于作业你只需要按照他的提示就可以本地评测，大大便利了我们的学习。`python3 ok --local`

4. lab, project的一些题目带有notes和hints，预判了学生可能踩入的一些坑并指出，有效地避免我们在做题时因为一些小问题而深陷困境难以自拔。

5. 对代码风格有较好的规范，~~至少对于我这种以前只会写让人血压升高的代码的人来说是大有帮助的~~。要有适当的空格分隔运算符和变量，函数名要反映功能，为函数写注释等等，还有最关键的data abstraction的思想，笔者认为这些对于养成良好的码风是相当重要的。

## 三、学习过程

1. 课程选择：笔者选择的是2020Fall的版本https://inst.eecs.berkeley.edu/~cs61a/fa20/ (其他版本修改后缀即可)个人比较推荐的是20fa和21fa的版本，讲师都是John DeNero，John DeNero的发音标准，而且语速偏慢，不用太担心听不懂的问题。而且他的讲课也很有意思，笔者印象最深的是他在讲到data abstraction时，说违背abstraction barrier的代码都应该用火烧掉。他也经常cue一些梗，虽然笔者不太懂但还是很有意思的，比许多催眠的老师好很多。（乐）

2. 相关配置：笔者使用的是WSL，Ubuntu20.04，使用的IDE是VSCode。相比Windows下编程，个人更加喜欢Linux环境。不过各种配置，在lab0有超详细的指导让你从零开始，一步一步地配好61A所需要的环境。

   <img src="C:\Users\HobbitQia\AppData\Roaming\Typora\typora-user-images\image-20220323135235911.png" alt="image-20220323135235911" style="zoom:50%;" />

3. 学习顺序：笔者基本上是按照reading-playlist（lecture）-lab-disc-hw-q&a-project，按照每天的任务依次完成即可。

   * 笔者认为reading是最精华的部分，可以看出教授改编经典教材是下了心思的。lecture可以用作补充，会有具体的代码示例，同时也会补充一些reading里没有的东西，而Q&A更多的是讨论上课/作业/往年考试的一些问题，也经常讨论一些有意思的话题。笔者记得在第六次课时Q&A下面已经有时间戳了，选择自己想看的问题即可。<img src="C:\Users\HobbitQia\AppData\Roaming\Typora\typora-user-images\image-20220323135539746.png" alt="image-20220323135539746" style="zoom:50%;" />
   * lab, disc, project，最好是都要做完，其中20fa的disc还是用pdf，要做的话只能自己写在纸上或者LaTeX编写（可惜笔者当时不会LaTeX），21年就有可以在线提交的方式了。此外project是最重要的锻炼自己的方式，上千行的start code，十几个子问题，能让你在实践中巩固所学。顺带一提，第四个project是用python写一个scheme的解释器，有前辈称61A3000刀，scheme这个project值2000刀，可见这个含金量是非常高的，虽然非常折磨（逃）

## 四、注意事项

1. 官方的solutions会在作业截止后公布，但是因为几乎每学期的作业都差不多，所以在课程结束后会全部下架。因此如果是跟最新的课建议每次的solutions先保存下来，如果是学以前的可以找找网上的资源（笔者有部分20fa和21fa的）官方的答案还是非常值得看的，写的非常简洁，值得我们好好借鉴学习。

2. 客观来说，61A的难度还是有的，~~也有可能是笔者太菜了~~。对于project来说，很大的问题在于读不懂题（特别是第一个project hog），加上题目背景和规则的描述又非常长，如果中途做了其他事后回来不太好找到本来的思路。笔者建议project就找整块时间开始一直做，不要有过长的中断，以保证思路的连贯。（当然大佬按照自己的节奏就行，仅供参考）例如，笔者写hog的时候从下午7点开始写，到晚上9.30去吃了晚饭，回来发现脑子空空什么的不记得了，后面因为对规则模糊卡了好久，直到第二天凌晨1.30才写完。而写最后的scheme时，笔者从下午1.开始，到晚上8.30时差不多剩了两道很难的题，剩下两道题又磨掉了第二天的上午和中午。

3. 一些具体的问题

   * 20fa的scheme的project里有关于tail call和macro的选做题，但是这些东西是放在很后面的optional lecture里的，如果不听lecture直接上手可能比较困难。根据笔者不完全统计，20su和21fa都是在scheme的project之前就讲了这方面的东西（个人猜测20fa可能是一次尝试？虽然之后又改回去了）

   * 20fa的lab12和lab14中，笔者下载下来的sqlite_shell.py里面是空的（可能是笔者自己的配置哪里出了问题，这里仅供参考，没有这方面问题可以跳过），导致无法测试自己的程序。笔者在折腾后从github上复制了别人的sqlite_shell.py就可以了。

## 五、后话

很幸运打开了61A的大门，徜徉在其中时，也不禁想到我们要走的路还有很长。世界一流名校，靠的不只是科研和论文，教学的质量同样重要。教育的本质是一棵树摇动一棵树，一朵云推动一朵云，一个灵魂唤醒一个灵魂，可以说CS61A真正让我感受到他们是在用心搞教育，用心教学生。有点羡慕那里点学生，通过这样的课程入门计算机，想必是一段极其美妙的开始吧。很感激他们能公开这样优质的课程，未来路还很长，诸君共勉。
