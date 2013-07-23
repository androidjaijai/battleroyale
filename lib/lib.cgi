# ���ѥ��֥롼����2

#==================#
# �� �ۥ���̾����  #
#==================#
sub GetHostName {
    my($ip_address) = @_;
    my(@addr) = split(/\./, $ip_address);
    my($packed_addr) = pack("C4", $addr[0], $addr[1], $addr[2], $addr[3]);
    my($name, $aliases, $addrtype, $length, @addrs);
    ($name, $aliases, $addrtype, $length, @addrs) = gethostbyaddr($packed_addr, 2);
    return $name;
}


#==================#
# �� �إå�����    #
#==================#
sub HEADER {
print "Content-type: text/html\n\n";
print <<"_HERE_";
<HTML>
<HEAD>
<META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=x-euc-jp">
<TITLE>$game</TITLE>
</HEAD>
<BODY bgcolor="#000000" text="#ffffff" link="#ff0000" vlink="#ff0000" style='font-size : 13px;font-family : "MS UI Gothic";font-weight : normal;font-style : normal;font-variant : normal;'>
<CENTER>
_HERE_
}
#==================#
# �� �եå���      #
#==================#
sub FOOTER {
print <<"_HERE_";
</CENTER>
<HR>
<DIV align="right"><B><A href="http://www.happy-ice.com/battle/">BATTLE ROYALE $ver</A></B></DIV>
</BODY>
</HTML>
_HERE_
}

#==================#
# �� ���顼����    #
#==================#
sub ERROR{#�����顼����
if ($lockflag) { &UNLOCK; }

$errmes = @_[0] ;
&HEADER;
print <<"_HERE_";
<B><FONT color="#ff0000" size="+2" face="�ͣ� ��ī">���顼ȯ��</FONT></B><BR><BR>
$errmes<BR>
<BR>
<B><FONT color="#ff0000"><A href="$home">HOME</A></B>
_HERE_
&FOOTER;
exit;
}

#====================#
# �� ����¸        #
#====================#
sub LOGSAVE {

    local($work) = @_[0] ;
    local($newlog) = "" ;

    if ($work eq "NEWENT") { #������Ͽ
        $newlog = "$now,$f_name2,$l_name2,$sex2,$cl,$no,,,,,$host2,ENTRY,$host,\n" ;
    } elsif ($work eq "DEATH" ){ #��ʬ��˴���װ���櫡������ڤ��
        $newlog = "$now,$f_name,$l_name,$sex,$cl,$no,,,,,,DEATH,$dmes,\n" ;
        $death = "����";$msg=$dmes;
    } elsif ($work eq "DEATH1" ){ #��ʬ��˴���װ����ǻ���
        $newlog = "$now,$f_name,$l_name,$sex,$cl,$no,,,,,,DEATH1,$dmes,\n" ;
        $death = "��ʪ�ݼ�";$msg=$dmes;
    } elsif ($work eq "DEATH2" ){ #��ʬ��˴���װ����Ի��
        local($w_name,$w_kind) = split(/<>/, $w_wep);
        if ($w_kind =~ /N/) {           #�·�
            $d2 = "�»�" ;
        } elsif (($w_kind =~ /A/) && ($w_wtai > 0)) {   #���
            $d2 = "�ͻ�" ;
        } elsif (($w_kind =~ /G/) && ($w_wtai > 0)) {   #�Ʒ�
            $d2 = "�ƻ�" ;
        } elsif ($w_kind =~ /C/) {  #���
            $d2 = "����" ;
        } elsif ($w_kind =~ /D/) {  #����
            $d2 = "����" ;
        } elsif ($w_kind =~ /S/) {  #�ɷ�
            $d2 = "�ɻ�" ;
        } elsif (($w_kind =~ /B/) || (($w_kind =~ /G|A/) && ($w_wtai == 0))) { #���� or ��̵���� or ��̵����
            $d2 = "�л�" ;
        } else {
            $d2 = "����" ;
        }

        $newlog = "$now,$f_name,$l_name,$sex,$cl,$no,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,DEATH2,$dmes,\n" ;
        if ($w_no eq "����") {
            $deth = "$w_f_name $w_l_name�ˤ��$d2";
        } else {
            $deth = "$w_f_name $w_l_name��$w_cl $w_sex$w_no�֡ˤˤ��$d2";
        }
        if ($w_msg ne "") {
            $msg = "$w_f_name $w_l_name��$w_msg��" ;
        } else {
            $msg = "" ;
        }
    } elsif ($work eq "DEATH3" ){ #Ũ��˴���װ����Ի��
        local($w_name,$w_kind) = split(/<>/, $wep);
        if ($w_kind =~ /N/) {           #�·�
            $d2 = "�»�" ;
        } elsif (($w_kind =~ /A/) && ($wtai > 0)) { #���
            $d2 = "�ͻ�" ;
        } elsif (($w_kind =~ /G/) && ($wtai > 0)) { #�Ʒ�
            $d2 = "�ƻ�" ;
        } elsif ($w_kind =~ /C/) {  #���
            $d2 = "����" ;
        } elsif ($w_kind =~ /D/) {  #����
            $d2 = "����" ;
        } elsif ($w_kind =~ /S/) {  #�ɷ�
            $d2 = "�ɻ�" ;
        } elsif (($w_kind =~ /B/) || (($w_kind =~ /G|A/) && ($wtai == 0))) { #���� or ��̵���� or ��̵����
            $d2 = "�л�" ;
        } else {
            $d2 = "����" ;
        }
        $newlog = "$now,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$f_name,$l_name,$sex,$cl,$no,DEATH3,$w_dmes,\n" ;
        $deth = "$f_name $l_name��$cl $sex$no�֡ˤˤ��$d2";
        if ($msg ne "") {
            $w_msg = "$f_name $l_name��$msg��" ;
        } else {
            $w_msg = "" ;
        }
        $w_log = "";
    } elsif ($work eq "DEATH4" ){ #���ܤˤ�뻦��
        $newlog = "$now,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,,,,,,DEATH4,$w_dmes,\n" ;
        $deth = "���ܤˤ��跺";
        $log ="";
        if ($w_msg ne "") {
            $msg = "���ܡ�$w_msg��" ;
        } else {
            $msg = "" ;
        }
    } elsif ($work eq "DEATH5" ){ #���ܤˤ�뻦��2
        $newlog = "$now,$f_name,$l_name,$sex,$cl,$no,,,,,,DEATH4,$dmes,\n" ;
        $deth = "���ܤˤ��跺";
        $log ="";
        $msg = "���ܡإ�����ʤ����Կ��ʹ�ư���ä�����ؤ����ˤ���äƸ��ä���ʡ�" ;
    } elsif ($work eq "DEATHAREA" ){ #��˴���װ����ػߥ��ꥢ��
        $newlog = "$now,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,,,,,,DEATHAREA,$w_dmes,\n" ;
        $deth = "�ػߥ��ꥢ�ں�";
        $msg = "" ;$log ="";
    } elsif ($work eq "WINEND1" ){ #ͥ������
        $newlog = "$now,$f_name,$l_name,$sex,$cl,$no,,,,,,WINEND,$dmes,\n" ;
        open(FLAG,">$end_flag_file"); print(FLAG "��λ\n"); close(FLAG);
    } elsif ($work eq "EX_END" ){ #�ϥå��󥰤ˤ��ץ��������
        $newlog = "$now,$f_name,$l_name,$sex,$cl,$no,,,,,,EX_END,$dmes,\n" ;
    } elsif ($work eq "AREAADD" ){ #�ػߥ��ꥢ�ɲ�
        $ar = $ar2 - 3 ;
        $newlog = "$now,$ar2,$ar,,,,,,,,,AREA,,\n" ;
    }

    open(DB,"$log_file") || exit; seek(DB,0,0); @loglist=<DB>; close(DB);
    unshift(@loglist,$newlog);

    open(DB,">$log_file"); seek(DB,0,0); print DB @loglist; close(DB);


}

#====================#
# �� LOCK            #
#====================#
sub LOCK {
    local($retry,$mtime);
    # 1ʬ�ʾ�Ť���å��Ϻ������
    if (-e $lockf) {
        ($mtime) = (stat($lockf))[9];
        if ($mtime < time - 60) { &UNLOCK; }
    }
    # symlink�ؿ�����å�
    if ($lkey == 1) {
        $retry = 5;
        while (!symlink(".", $lockf)) {
            if (--$retry <= 0) { &ERROR("�����������Ѻ��߹�äƤ���ޤ������Ф餯���Ԥ���������"); }
            sleep(1);
        }
    # mkdir�ؿ�����å�
    } elsif ($lkey == 2) {
        $retry = 5;
        while (!mkdir($lockf, 0755)) {
            if (--$retry <= 0) {  &ERROR("�����������Ѻ��߹�äƤ���ޤ������Ф餯���Ԥ���������"); }
            sleep(1);
        }
    # Tripod�ѡʻ����
    } elsif ($lkey == 3) {
        local($lk) = mkdir($lockf, 0755);
        if ($lk == 0) {  &ERROR("�����������Ѻ��߹�äƤ���ޤ������Ф餯���Ԥ���������"); }
    }
    $lockflag=1;
}

#====================#
# �� UNLOCK          #
#====================#

sub UNLOCK {
    if ($lkey == 1) { unlink($lockf); }
    elsif ($lkey == 2) { rmdir($lockf); }
    elsif ($lkey == 3) { rmdir($lockf); }
    $lockflag=0;
}

1
