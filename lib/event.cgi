#==================#
# �� ���٥�Ƚ���  #
#==================#
sub EVENT {

    local($dice) = int(rand(5)) ;
    local($dice2) = int(rand(5)+5) ;
    $Command = "MAIN";
    if ($dice < 2) {return ; }


    if ($pls == 0) {    #ʬ��




    } elsif ($pls == 1) {   #�̤�̨


    } elsif ($pls == 2) {   #����¼����
        $log = ($log . "�դȡ����򸫾夲��ȡ����η������<BR>") ;
        if ($dice == 2) {
            $log = ($log . "���˽���졢Ƭ�����������<BR>") ;
            $inf =~ s/Ƭ//g ;
            $inf = ($inf . "Ƭ") ;
        } elsif ($dice == 3) {
            $log = ($log . "���˽���졢<font color=\"red\"><b>$dice2���᡼��</b></font> ���������<BR>") ;
            $hit-=$dice2;
            if ($hit <= 0) {
                $hit = $mhit = 0;
                $log = ($log . "<font color=\"red\"><b>$f_name $l_name��$cl $sex$no�֡ˤϻ�˴������</b></font><br>") ;

                #��˴��
                &LOGSAVE("DEATH") ;
                $Command = "EVENT";
            }
        } else {
        $log = ($log . "�դ����ʤ�Ȥ����ष����������<BR>") ;
        }
        $chksts="OK";
    } elsif ($pls == 3) {   #����¼���
    } elsif ($pls == 4) {   #͹�ض�
    } elsif ($pls == 5) {   #���ɽ�
    } elsif ($pls == 6) {   #�Ѳ�Ʋ
    } elsif ($pls == 7) {   #�⸶��
    } elsif ($pls == 8) {   #��������
    } elsif ($pls == 9) {   #�ۥƥ���
    } elsif ($pls == 10) {  #��������
        $log = ($log . "���ޤä����ں��������<BR>") ;
        if ($dice == 2) {
            $log = ($log . "���Ȥ����路���������Ф�­�����������<BR>") ;
            $inf =~ s/­//g ;
            $inf = ($inf . "­") ;
        } elsif ($dice == 3) {
            $log = ($log . "���Фˤ�ꡢ<font color=\"red\"><b>$dice2���᡼��</b></font> ���������<BR>") ;
            $hit-=$dice2;
            if ($hit <= 0) {
                $hit = $mhit = 0;
                $log = ($log . "<font color=\"red\"><b>$f_name $l_name��$cl $sex$no�֡ˤϻ�˴������</b></font><br>") ;

                #��˴��
                &LOGSAVE("DEATH") ;
                $Command = "EVENT";
            }
        } else {
            $log = ($log . "�դ����ʤ�Ȥ����路����������<BR>") ;
        }
        $chksts="OK";
    } elsif ($pls == 11) {  #�ȥ�ͥ�
    } elsif ($pls == 12) {  #ʿ��¼����
        $log = ($log . "�դȡ����򸫾夲��ȡ����η������<BR>") ;
        if ($dice == 2) {
            $log = ($log . "���˽���졢Ƭ�����������<BR>") ;
            $inf =~ s/Ƭ//g ;
            $inf = ($inf . "Ƭ") ;
        } elsif ($dice == 3) {
            $log = ($log . "���˽���졢<font color=\"red\"><b>$dice2���᡼��</b></font> ���������<BR>") ;
            $hit-=$dice2;
            if ($hit <= 0) {
                $hit = $mhit = 0;
                $log = ($log . "<font color=\"red\"><b>$f_name $l_name��$cl $sex$no�֡ˤϻ�˴������</b></font><br>") ;

                #��˴��
                &LOGSAVE("DEATH") ;
                $Command = "EVENT";
            }
        } else {
            $log = ($log . "�դ����ʤ�Ȥ����ष����������<BR>") ;
        }
        $chksts="OK";
    } elsif ($pls == 13) {  #̵�ػ�
    } elsif ($pls == 14) {  #ʬ����
    } elsif ($pls == 15) {  #�������
    } elsif ($pls == 16) {  #��������
        $log = ($log . "��ǡ����������ݤ��äƤ�����<BR>") ;
        if ($dice == 2) {
            $log = ($log . "�Ӥ򤫤ޤ졢�Ӥ����������<BR>") ;
            $inf =~ s/��//g ;
            $inf = ($inf . "��") ;
        } elsif ($dice == 3) {
            $log = ($log . "��˽���졢<font color=\"red\"><b>$dice2���᡼��</b></font> ���������<BR>") ;
            $hit-=$dice2;
            if ($hit <= 0) {
                $hit = $mhit = 0;
                $log = ($log . "<font color=\"red\"><b>$f_name $l_name��$cl $sex$no�֡ˤϻ�˴������</b></font><br>") ;

                #��˴��
                &LOGSAVE("DEATH") ;
                $Command = "EVENT";
            }
        } else {
            $log = ($log . "�դ����ʤ�Ȥ����ष����������<BR>") ;
        }
        $chksts="OK";
    } elsif ($pls == 17) {  #����Ϻ��
        $log = ($log . "���ޤä���­���餻����<BR>") ;
        if ($dice <= 3) {
            $dice2 += 10;
            $log = ($log . "�Ӥ��������������ʤ�Ȥ��礤�夬�ä���<BR>�����ߥʤ� <font color=\"red\"><b>$dice2�ݥ����</b></font> ���񤷤���<BR>") ;
            $sta-=$dice2;
            if ($sta <= 0) {    #�����ߥ��ڤ졩
                &DRAIN("eve");
            }
        } else {
            $log = ($log . "�դ����ʤ��������˺Ѥ����������<BR>") ;
        }
        $chksts="OK";
    } elsif ($pls == 18) {  #ɹ��¼����
        $log = ($log . "�դȡ����򸫾夲��ȡ����η������<BR>") ;
        if ($dice == 2) {
            $log = ($log . "���˽���졢Ƭ�����������<BR>") ;
            $inf =~ s/Ƭ//g ;
            $inf = ($inf . "Ƭ") ;
        } elsif ($dice == 3) {
            $log = ($log . "���˽���졢<font color=\"red\"><b>$dice2���᡼��</b></font> ���������<BR>") ;
            $hit-=$dice2;
            if ($hit <= 0) {
                $hit = $mhit = 0;
                $log = ($log . "<font color=\"red\"><b>$f_name $l_name��$cl $sex$no�֡ˤϻ�˴������</b></font><br>") ;

                #��˴��
                &LOGSAVE("DEATH") ;
                $Command = "EVENT";
            }
        } else {
            $log = ($log . "�դ����ʤ�Ȥ����ष����������<BR>") ;
        }
        $chksts="OK";
    } elsif ($pls == 19) {  #���Ž�
    } elsif ($pls == 20) {  #����
    } elsif ($pls == 21) {  #���̨
    }
}

1