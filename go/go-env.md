# go 配置环境

`$ go env`

## [GOPATH](https://golang.org/cmd/go/#hdr-GOPATH_environment_variable)

$HOME/go on Unix, $home/go on Plan 9, and %USERPROFILE%\go (usually C:\Users\YourName\go) on Windows.

## bin

`$ export PATH=$PATH:$(go env GOPATH)/bin`

bin contains executable commands

## remote repository

```bash
$ cd $GOPATH/src/github.com/user/hello
$ git init
Initialized empty Git repository in /home/user/work/src/github.com/user/hello/.git/
$ git add hello.go
$ git commit -m "initial commit"
[master (root-commit) 0b4507d] initial commit
 1 file changed, 1 insertion(+)
  create mode 100644 hello.go
```
