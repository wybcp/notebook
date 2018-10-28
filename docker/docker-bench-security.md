# [The Docker Bench for Security](https://github.com/docker/docker-bench-security)

The Docker Bench for Security is a script that checks for dozens of common best-practices around deploying Docker containers in production.

```bash
docker run -it --net host --pid host --userns host --cap-add audit_control \
    -e DOCKER_CONTENT_TRUST=$DOCKER_CONTENT_TRUST \
    -v /var/lib:/var/lib \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v /usr/lib/systemd:/usr/lib/systemd \
    -v /etc:/etc --label docker_bench_security \
    docker/docker-bench-security
```

Docker bench requires Docker 1.13.0 or later in order to run.

输出结果中，带有不同的级别，说明问题的严重程度，最后会给出整体检查结果和评分。一般要尽量避免出现 WARN 或以上的问题。
