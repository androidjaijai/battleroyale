#! /usr/local/bin/perl
require "jcode.pl";
require "br.cgi";
require "$LIB_DIR/lib.cgi";
&LOCK;
require "pref.cgi";



    open(DB,"$log_file");seek(DB,0,0); @loglist=<DB>;close(DB);

    ($ar[0],$ar[1],$ar[2],$ar[3],$ar[4],$ar[5],$ar[6],$ar[7],$ar[8],$ar[9],$ar[10],$ar[11],$ar[12],$ar[13],$ar[14],$ar[15],$ar[16],$ar[17],$ar[18],$ar[19],$ar[20],$ar[21],$ar[22]) = split(/,/, $arealist[4]);

    $getmonth=$getday=0;
    foreach $loglist(@loglist) {
        ($gettime,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_f_name2,$w_l_name2,$w_sex2,$w_cl2,$w_no2,$getkind,$host)= split(/,/, $loglist);
        ($sec,$min,$hour,$mday,$month,$year,$wday,$yday,$isdst) = localtime($gettime);
        $hour = "0$hour" if ($hour < 10);
        $min = "0$min" if ($min < 10);  $month++;
        $year += 1900;
        $week = ('��','��','��','��','��','��','��') [$wday];
        if (($getmonth != $month) || ($getday != $mday)) {
            if ($getmonth !=0) { push (@log,"</LI></UL>\n"); }
            $getmonth=$month;$getday = $mday;
            push (@log,"<P><font color=\"lime\"><B>$month�� $mday�� ($week����)</B></font><BR>\n");
            push (@log,"<UL>\n");
        }

        if ($host eq "") { $host = ""; } else { $host = "($host)" ; }
        if((!$host_view)&&($getkind eq "ENTRY")){$host = "";}

        if ($getkind eq "DEATH") {  #��˴�ʼ�ʬ��������
            push (@log,"<LI>$hour��$minʬ��<font color=\"red\"><b>$w_f_name $w_l_name��$w_cl $w_sex$w_no�֡�</b></font> �� ��˴������<font color=\"red\"><b>$host</b></font><BR>\n") ;
        } elsif ($getkind eq "DEATH1") { #��˴���ǻ���
            push (@log,"<LI>$hour��$minʬ��<font color=\"red\"><b>$w_f_name $w_l_name��$w_cl $w_sex$w_no�֡�</b></font> �� ��˴������<font color=\"red\"><b>$host</b></font><BR>\n") ;
        } elsif ($getkind eq "DEATH2") { #��˴��¾����
            push (@log,"<LI>$hour��$minʬ��<font color=\"red\"><b>$w_f_name $w_l_name��$w_cl $w_sex$w_no�֡�</b></font> �� ��˴������<font color=\"red\"><b>$host</b></font><BR>\n") ;
        } elsif ($getkind eq "DEATH3") { #��˴��¾����
            push (@log,"<LI>$hour��$minʬ��<font color=\"red\"><b>$w_f_name $w_l_name��$w_cl $w_sex$w_no�֡�</b></font> �� ��˴������<font color=\"red\"><b>$host</b></font><BR>\n") ;
        } elsif ($getkind eq "DEATH4") { #��˴�����ܡ�
            push (@log,"<LI>$hour��$minʬ��<font color=\"red\"><b>$w_f_name $w_l_name��$w_cl $w_sex$w_no�֡�</b></font> �� ��˴������<font color=\"red\"><b>$host</b></font><BR>\n") ;
        } elsif ($getkind eq "DEATHAREA") { #��˴�ʶػߥ��ꥢ��
            push (@log,"<LI>$hour��$minʬ��<font color=\"red\"><b>$w_f_name $w_l_name��$w_cl $w_sex$w_no�֡�</b></font> �� �ػߥ��ꥢ�ΰ١���˴������<font color=\"red\"><b>$host</b></font><BR>\n") ;
        } elsif ($getkind eq "WINEND") { #ͥ���Է���
            $log_num = pop @log;
            if ($log_num =~ /�����ཪλ/){
                push (@log,$log_num);
            }else{
                push (@log,$log_num);
                push (@log,"<LI>$hour��$minʬ��<font color=\"lime\"><b>�����ཪλ���ʾ��ܥץ����»����������ǧ��˥����</B></font> <BR>\n") ;
            }
        } elsif ($getkind eq "EX_END") { #�ץ�������
            $log_num = pop @log;
            if ($log_num =~ /�����ཪλ/){
                push (@log,$log_num);
            }else{
                push (@log,$log_num);
                push (@log,"<LI>$hour��$minʬ��<font color=\"lime\"><b>�����ཪλ���ץ����۵����</B></font> <BR>\n") ;
            }
        } elsif ($getkind eq "AREA") { #�ػߥ��ꥢ�ɲ�
            $log_num = pop @log;
            if (($log_num !~ /�����ཪλ/)||($log_num !~ /<UL>/)){
                push (@log,$log_num);
                push (@log,"<LI>$hour��$minʬ��<font color=\"lime\"><b>$place[$ar[$w_l_name]]��$place[$ar[$w_l_name+1]]��$place[$ar[$w_l_name+2]]</b></font> �� �ػߥ��ꥢ�˻��ꤵ�줿������ػߥ��ꥢ��<font color=\"lime\"><b>$place[$ar[$w_f_name]]��$place[$ar[$w_f_name+1]]��$place[$ar[$w_f_name+2]]</b></font>��<BR>\n") ;
            }else{
                push (@log,$log_num);
            }
        } elsif ($getkind eq "ENTRY") { #������Ͽ
            push (@log,"<LI>$hour��$minʬ��<font color=\"yellow\"><b>$w_f_name $w_l_name��$w_cl $w_sex$w_no�֡�</b></font> �� ž�����Ƥ�����$host<BR>\n") ;
        } elsif ($getkind eq "NEWGAME") { #�����ͤˤ��ǡ��������
            push (@log,"<LI>$hour��$minʬ�������ץ���೫�ϡ�<BR>\n") ;
        }

        $cnt++;
    }

    for ($i=0; $i<$arealist[1]  ; $i++) {
        $ars = ($ars . " $place[$ar[$i]]") ;
    }
    $ars = "<BR><font color=\"lime\"><B>���ߤζػߥ��ꥢ</B></FONT>  $ars<BR><font color=\"lime\"><B>����ζػߥ��ꥢ</B></FONT>  $place[$ar[$i]] $place[$ar[$i+1]] $place[$ar[$i+2]]\n" ;


    &HEADER ;
    print "</center>\n" ;
    print "<B><FONT color=\"#ff0000\" size=\"+3\" face=\"�ͣ� ��ī\">�ʹԾ���</FONT></B><BR><BR>\n";
    print "�ؤߤ�ʡ��������ˤ�äƤ뤫����<BR>���줸�㡢����ޤǤξ����ǡ�����<BR>�������������Ф��ʡ�����<br>\n";
    print "$ars";
    print @log;
    print "<center>\n" ;
    print "<BR><B><a href=\"index.htm\">HOME</A></B><BR>\n";

    &FOOTER;
&UNLOCK;

exit;
