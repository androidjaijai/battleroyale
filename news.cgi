#!/usr/bin/perl
require "jcode.pl";
require "br.cgi";
require "$LIB_DIR/lib.cgi";
&LOCK;
require "pref.cgi";

    open(DB,"$log_file");seek(DB,0,0); @loglist=<DB>;close(DB);

    @ar = split(/,/, $arealist[4]);

    $getmonth=$getday=0;
    foreach $loglist(@loglist) {
        ($gettime,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_f_name2,$w_l_name2,$w_sex2,$w_cl2,$w_no2,$getkind,$info1,$info2,$info3)= split(/,/, $loglist);
        ($sec,$min,$hour,$mday,$month,$year,$wday,$yday,$isdst) = localtime($gettime);
        $hour = sprintf("%02d", $hour);
        $min  = sprintf("%02d", $min);
        $month++; $year += 1900;
        $week = ('��','��','��','��','��','��','��') [$wday];
        if (($getmonth != $month) || ($getday != $mday)) {
            if ($getmonth !=0) { push (@log,"</LI></UL>\n"); }
            $getmonth=$month;$getday = $mday;
            push (@log,"<P><font color=\"lime\"><B>$month�� $mday�� ($week����)</B></font><BR>\n");
            push (@log,"<UL>\n");
        }

        if ($info1 ne "") { $info1 = "($info1)" ; }

        if ($getkind eq "DEATH") {  #��˴�ʼ�ʬ��������
            push (@log,"<LI>$hour��$minʬ��<font color=\"red\"><b>$w_f_name $w_l_name��$w_cl $w_sex$w_no�֡�</b></font>��<font color=\"red\"><b>��˴</b></font>������<font color=\"red\"><b>$info1</b></font><BR>\n") ;
        } elsif ($getkind eq "DEATH1") { #��˴���ǻ���
            push (@log,"<LI>$hour��$minʬ��<font color=\"red\"><b>$w_f_name $w_l_name��$w_cl $w_sex$w_no�֡�</b></font>��<font color=\"red\"><b>���ǻ�</b></font>������<font color=\"red\"><b>$info1</b></font><BR>\n") ;
        } elsif ($getkind eq "DEATH2") { #��˴��¾����
            push (@log,"<LI>$hour��$minʬ��<font color=\"red\"><b>$w_f_name $w_l_name��$w_cl $w_sex$w_no�֡�</b></font>��<font color=\"yellow\"><b>$w_f_name2 $w_l_name2��$w_cl2 $w_sex2$w_no2�֡�</b></font>��<font color=\"aqua\"><b>$info2</b></font>��<font color=\"red\"><b>�֤�Ƥ��</b></font>�ˤ��줿��<font color=\"red\"><b>$info1</b></font><BR>\n") ;
        } elsif ($getkind eq "DEATH3") { #��˴��¾����
            push (@log,"<LI>$hour��$minʬ��<font color=\"red\"><b>$w_f_name $w_l_name��$w_cl $w_sex$w_no�֡�</b></font>��<font color=\"yellow\"><b>$w_f_name2 $w_l_name2��$w_cl2 $w_sex2$w_no2�֡�</b></font>��<font color=\"aqua\"><b>$info2</b></font>��<font color=\"red\"><b>$info3</b></font>���줿��<font color=\"red\"><b>$info1</b></font><BR>\n") ;
        } elsif ($getkind eq "DEATH4") { #��˴�����ܡ�
            push (@log,"<LI>$hour��$minʬ��<font color=\"red\"><b>$w_f_name $w_l_name��$w_cl $w_sex$w_no�֡�</b></font>�����ܤ�<font color=\"red\"><b>�跺</b></font>���줿��<font color=\"red\"><b>$info1</b></font><BR>\n") ;
        } elsif ($getkind eq "DEATHAREA") { #��˴�ʶػߥ��ꥢ��
            push (@log,"<LI>$hour��$minʬ��<font color=\"red\"><b>$w_f_name $w_l_name��$w_cl $w_sex$w_no�֡�</b></font>��<font color=\"red\"><b>�ػߥ��ꥢ</b></font>�ΰ١���˴������<font color=\"red\"><b>$info1</b></font><BR>\n") ;
        } elsif ($getkind eq "WINEND") { #ͥ���Է���
            push (@log,"<LI>$hour��$minʬ��<font color=\"lime\"><b>�����ཪλ���ʾ��ܥץ����»����������ǧ��˥����</B></font> <BR>\n") ;
        } elsif ($getkind eq "EX_END") { #�ץ�������
            push (@log,"<LI>$hour��$minʬ��<font color=\"lime\"><b>$w_f_name $w_l_name��$w_cl $w_sex$w_no�֡ˤ��ץ��������������ѡ��ץ����۵����</B></font> <BR>\n") ;
        } elsif ($getkind eq "HACK") { #�ϥå���
            push (@log,"<LI>$hour��$minʬ��<font color=\"lime\"><b>$w_f_name $w_l_name��$w_cl $w_sex$w_no�֡ˤˤ�äƥϥå��󥰤������ʬ���ε�ǽ����ߡ���</B></font> <BR>\n") ;
        } elsif ($getkind eq "SPEAKER") { #����
            push (@log,"<LI>$hour��$minʬ��<font color=\"aqua\"><b>$w_f_name $w_l_name��$w_cl $w_sex$w_no�֡�</b></font> �� <font color=\"aqua\"><b>$info1</b></font> �ȶ������<BR>\n") ;
        } elsif ($getkind eq "AREA") { #�ػߥ��ꥢ�ɲ�
            if ($info2 == 7) {
                push (@log,"<LI>$hour��$minʬ��<font color=\"lime\"><b>�ץ����ǽ�������</b></font>��<BR>\n") ;
            } elsif ($info2 == 8) {
                push (@log,"<LI>$hour��$minʬ��<font color=\"lime\"><b>�����ڤ�ˤ�ꥲ���ཪλ</b></font>��<BR>\n") ;
            } else {
                push (@log,"<LI>$hour��$minʬ��<font color=\"lime\"><b>�ץ����$info2���ܳ���</b></font>��<BR>\n") ;
            }
        } elsif ($getkind eq "ENTRY") { #������Ͽ
            push (@log,"<LI>$hour��$minʬ��<font color=\"yellow\"><b>$w_f_name $w_l_name��$w_cl $w_sex$w_no�֡�</b></font> �� ž�����Ƥ�����<font color=\"yellow\">$info1</font><BR>\n") ;
        } elsif ($getkind eq "NEWGAME") { #�����ͤˤ��ǡ��������
            push (@log,"<LI>$hour��$minʬ��<font color=\"lime\"><b>�����ץ���೫��</b></font>��<BR>\n") ;
        }

        $cnt++;
    }

    if ($hackflg) {
        $ars1 = "�ʤ�";
        for ($i=0; $i<$ar+3  ; $i++) {
            $ars2 .= " $place[$ar[$i]]";
        }
    } else {
        for ($i=0; $i<$ar; $i++) {
            $ars1 .= " $place[$ar[$i]]";
        }
        for ($i=$ar; $i<$ar+3; $i++) {
            $ars2 .= " $place[$ar[$i]]";
        }
    }
    $ars = "<BR><font color=\"lime\"><B>���ߤζػߥ��ꥢ</B></FONT>  $ars1<BR><font color=\"lime\"><B>����ζػߥ��ꥢ</B></FONT>  $ars2\n" ;

    &HEADER ;
    print "</center>\n" ;
    print "<B><FONT color=\"#ff0000\" size=\"+3\" face=\"�ͣ� ��ī\">�ʹԾ���</FONT></B><BR><BR>\n";
    print "<table><tr><td width=\"70\" height=\"70\"><img src=\"$imgurl$n_icon_file[0]\"></td><td>�ؤߤ�ʡ��������ˤ�äƤ뤫����<BR>���줸�㡢����ޤǤξ����ǡ�����<BR>�������������Ф��ʡ�����</td></tr></table><br>\n";
    print "$ars";
    print @log;
    print "</UL>\n<center>\n" ;
    print "<B><a href=\"$home\">HOME</A></B><BR>\n";

    &FOOTER;
&UNLOCK;

exit;
