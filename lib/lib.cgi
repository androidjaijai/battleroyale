# ���ѥ��֥롼����2

#==================#
# �� �إå�����    #
#==================#
sub HEADER {
print "Content-type: text/html\n\n";
print <<"_HERE_";
<HTML>
<HEAD>
<META HTTP-EQUIV="Content-type" CONTENT="text/html; charset=euc-jp">
<TITLE>$game</TITLE>
<SCRIPT language="JavaScript">
<!--
    function sl(x) {
        document.f1.Command[x].checked = true;
    }
    function dbk(){
        window.alert("���֥륯��å��϶ػߤǤ���");
    }
//-->
</SCRIPT>
<STYLE type="text/css">
<!--
BODY {
    FONT-SIZE   : 9pt;
    font-family : "MS UI Gothic";
}
TH {
    FONT-SIZE:      9pt;
    BACKGROUND:     #005; 
    BORDER-RIGHT:   #336 1px solid; 
    BORDER-TOP:     #99c 1px solid; 
    BORDER-LEFT:    #99c 1px solid; 
    BORDER-BOTTOM:  #336 1px solid; 
}
TD      { FONT-SIZE: 9pt; }
A:hover { COLOR: #ffff99 }
-->
</STYLE>
</HEAD>
<BODY bgcolor="#000000" text="#ffffff" link="#ff0000" vlink="#ff0000">
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
<DIV align="right"><B><A href="http://www.happy-ice.com/battle/">BATTLE ROYALE V01.19</A></B></DIV>
</BODY>
</HTML>
_HERE_
}

#==================#
# �� ���顼����    #
#==================#
sub ERROR{
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
        $newlog = "$now,$f_name2,$l_name2,$sex2,$cl,$no,,,,,$host2,ENTRY,$host,$os,,\n" ;
    } elsif ($work eq "DEATH" ){ #��ʬ��˴���װ���櫡������ڤ��
        $newlog = "$now,$f_name,$l_name,$sex,$cl,$no,,,,,,DEATH,$dmes,,,\n" ;
        $death = "����";$msg=$dmes;
    } elsif ($work eq "DEATH1" ){ #��ʬ��˴���װ����ǻ���
        $newlog = "$now,$f_name,$l_name,$sex,$cl,$no,,,,,,DEATH1,$dmes,,,\n" ;
        $death = "��ʪ�ݼ�";$msg=$dmes;
    } elsif ($work eq "DEATH2" ){ #��ʬ��˴���װ����Ի��
        if ($w_kind2 =~ /N/) {           #�·�
            $d2 = "�»�" ;
        } elsif (($w_kind2 =~ /A/) && ($w_wtai > 0)) {   #���
            $d2 = "�ͻ�" ;
        } elsif (($w_kind2 =~ /G/) && ($w_wtai > 0)) {   #�Ʒ�
            $d2 = "�ƻ�" ;
        } elsif ($w_kind2 =~ /C/) {  #���
            $d2 = "����" ;
        } elsif ($w_kind2 =~ /D/) {  #����
            $d2 = "����" ;
        } elsif ($w_kind2 =~ /S/) {  #�ɷ�
            $d2 = "�ɻ�" ;
        } elsif (($w_kind2 =~ /B/) || (($w_kind2 =~ /G|A/) && ($w_wtai == 0))) { #���� or ��̵���� or ��̵����
            $d2 = "�л�" ;
        } else {
            $d2 = "����" ;
        }

        $newlog = "$now,$f_name,$l_name,$sex,$cl,$no,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,DEATH2,$dmes,$w_name2,,\n" ;
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
        $newlog = "$now,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$f_name,$l_name,$sex,$cl,$no,DEATH3,$w_dmes,$w_name,$d2,\n" ;
        $deth = "$f_name $l_name��$cl $sex$no�֡ˤˤ��$d2";
        if ($msg ne "") {
            $w_msg = "$f_name $l_name��$msg��" ;
        } else {
            $w_msg = "" ;
        }
    } elsif ($work eq "DEATH4" ){ #���ܤˤ�뻦��
        $newlog = "$now,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,,,,,,DEATH4,$w_dmes,,,\n" ;
        $deth = "���ܤˤ��跺";
        $log ="";
        if ($w_msg ne "") {
            $msg = "���ܡ�$w_msg��" ;
        } else {
            $msg = "" ;
        }
    } elsif ($work eq "DEATH5" ){ #���ܤˤ�뻦��2
        $newlog = "$now,$f_name,$l_name,$sex,$cl,$no,,,,,,DEATH4,$dmes,,,\n" ;
        $deth = "���ܤˤ��跺";
        $log ="";
        $msg = "���ܡإ�����ʤ����Կ��ʹ�ư���ä�����ؤ����ˤ���äƸ��ä���ʡ�" ;
    } elsif ($work eq "DEATHAREA" ){ #��˴���װ����ػߥ��ꥢ��
        $newlog = "$now,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,,,,,,DEATHAREA,$w_dmes,,,\n" ;
        $deth = "�ػߥ��ꥢ�ں�";
        $msg = "" ;$log ="";
    } elsif ($work eq "WINEND1" ){ #ͥ������
        $newlog = "$now,$f_name,$l_name,$sex,$cl,$no,,,,,,WINEND,$dmes,,,\n" ;
        open(FLAG,">$end_flag_file"); print(FLAG "��λ\n"); close(FLAG);
        require "$LIB_DIR/adlib.cgi";
        &InitResetTime;
    } elsif ($work eq "EX_END" ){ #�ץ��������
        $newlog = "$now,$f_name,$l_name,$sex,$cl,$no,,,,,,EX_END,$dmes,,,\n" ;
        require "$LIB_DIR/adlib.cgi";
        &InitResetTime;
    } elsif ($work eq "HACK" ){ #�ϥå���
        $newlog = "$now,$f_name,$l_name,$sex,$cl,$no,,,,,,HACK,,,,\n" ;
    } elsif ($work eq "SPEAKER" ){ #����
        $newlog = "$now,$f_name,$l_name,$sex,$cl,$no,,,,,,SPEAKER,$speech,,,\n" ;
    } elsif ($work eq "AREAADD" ){ #�ػߥ��ꥢ�ɲ�
        $ar = $ar2 - 3 ;
        $newlog = "$now,$ar2,$ar,,,,,,,,,AREA,,$pgday,,\n" ;
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
    }
    $lockflag=1;
}

#====================#
# �� UNLOCK          #
#====================#

sub UNLOCK {
    if ($lkey == 1) { unlink($lockf); }
    elsif ($lkey == 2) { rmdir($lockf); }
    $lockflag=0;
}

1
