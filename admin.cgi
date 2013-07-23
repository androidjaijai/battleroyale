#!/usr/bin/perl
require "jcode.pl";
require "br.cgi";
require "$LIB_DIR/lib.cgi";
require "$LIB_DIR/lib2.cgi";
require "$LIB_DIR/adlib.cgi";
&LOCK;
require "pref.cgi";

    &ADMDECODE ;
    # GET �᥽�åɤ����
    if ($Met_Post && !$p_flag) {
        &ERROR("�����ʥ��������Ǥ���");
    }

    if ($admpass ne $a_pass){
        $rogindat = "$now,$year/$month/$mday $hour:$min:$sec,$admpass,$host,FAILED,\n";
        open(DB,">>$A_Rogin_file"); seek(DB,0,0); print DB $rogindat; close(DB);
        &MAIN;&UNLOCK;exit;
    }

    $rogindat = "$now,$year/$month/$mday $hour:$min:$sec,$admpass,$host,$Command,\n";
    open(DB,">>$A_Rogin_file"); seek(DB,0,0); print DB $rogindat; close(DB);

    if ($Command eq "MAIN") {
        &MENU ;
    } elsif ($Command eq "BSAVE") {
        &BACKSAVE;
    } elsif ($Command eq "BREAD") {
        &BACKREAD;
    } elsif ($Command eq "RESINI") {
        &INITFORM;
    } elsif ($Command eq "RESINI2") {
        &RESINIT;
    } elsif ($Command eq "RESET") {
        &DATARESET;
        push(@log,"<B><FONT color=\"#ff0000\" size=\"+3\" face=\"�ͣ� ��ī\">�����⡼��</FONT></B><BR><BR>\n");
        push(@log,"��������ޤ�����<br>\n");
        push(@log,"<br><B><FONT color=\"#ff0000\">>><a href=\"$home\">HOME</a> >><a href=\"$adm\">ADMIN</a></b></FONT>\n");
        &HEADER; print @log; &FOOTER;
    } elsif ($Command eq "USERLIST") {
        &USERLIST;
    } elsif ($Command eq "USERDEL") {
        &USERDEL;
    } elsif ($Command eq "WINLOG") {
        &WINLOG;
    } elsif ($Command eq "LOGON") {
        &MAIN;
    } else { &MAIN; }
&UNLOCK;

exit;

#==================#
# �� �ᥤ��ǽ    #
#==================#
sub MAIN {

    push(@log,"<B><FONT color=\"#ff0000\" size=\"+3\" face=\"�ͣ� ��ī\">�����⡼��</FONT></B><BR><BR>\n");
    push(@log,"�����ѥѥ����\n");
    push(@log,"<FORM METHOD=\"POST\">\n");
    push(@log,"<INPUT TYPE=\"HIDDEN\" NAME=\"Command\" VALUE=\"MAIN\">\n");
    push(@log,"<INPUT size=\"16\" type=\"text\" name=\"Password\" maxlength=\"16\">\n");
    push(@log,"��<INPUT type=\"submit\" name=\"Enter\" value=\"����\">\n");
    push(@log,"</FORM>\n");

    &HEADER ;
    print @log;
    &FOOTER;
}
#==================#
# �� �ᥤ��ǽ    #
#==================#
sub MENU {

    $nowtime = sprintf("%04dǯ%02d��%02d����%s��%02d:%02d:%02d", $year, $month, $mday, ('��','��','��','��','��','��','��') [$wday], $hour, $min, $sec);
    push(@log,"<B><FONT color=\"#ff0000\" size=\"+3\" face=\"�ͣ� ��ī\">�����⡼��</FONT></B><BR><BR>\n$nowtime<BR>\n");
    push(@log,"<FORM METHOD=\"POST\">\n");
    push(@log,"<TABLE border=\"0\">\n");
    push(@log,"<TR><TD>\n");
    push(@log,"<INPUT type=\"hidden\" name=\"Password\" value=\"$admpass\">\n");
    push(@log,"<INPUT type=\"radio\" name=\"Command\" value=\"USERLIST\">�桼������<BR>\n");
    push(@log,"<INPUT type=\"radio\" name=\"Command\" value=\"BSAVE\">�Хå����å���¸<BR>\n");
    push(@log,"<INPUT type=\"radio\" name=\"Command\" value=\"BREAD\">�Хå����å��ɹ�<BR>\n");
    push(@log,"<INPUT type=\"radio\" name=\"Command\" value=\"WINLOG\">ͥ���������<BR>\n");
    push(@log,"<INPUT type=\"radio\" name=\"Command\" value=\"RESINI\">�������������<BR>\n");
    push(@log,"<INPUT type=\"radio\" name=\"Command\" value=\"RESET\">�ǡ��������<BR>\n");
    push(@log,"</TD></TR>\n");
    push(@log,"</TABLE>\n");
    push(@log,"<BR><INPUT type=\"submit\" name=\"Enter\" value=\"����\">\n");
    push(@log,"</FORM>\n");

    &HEADER ;
    print @log;
    &FOOTER;
}
#==================#
# �� �Хå����å���¸  #
#==================#
sub BACKSAVE {

    open(DB,">$back_file"); seek(DB,0,0); print DB @userlist; close(DB);

    push(@log,"<B><FONT color=\"#ff0000\" size=\"+3\" face=\"�ͣ� ��ī\">�����⡼��</FONT></B><BR><BR>\n");
    push(@log,"�Хå����åפ�������ޤ�����<br>\n");

    &HEADER ;
    print @log;
    print "<br><B><FONT color=\"#ff0000\">>><a href=\"$home\">HOME</a> >><a href=\"$adm\">ADMIN</a></b></FONT>\n";
    &FOOTER;

}
#==================#
# �� �Хå����å��ɹ�  #
#==================#
sub BACKREAD {

    open(DB,"$back_file");seek(DB,0,0); @userlist=<DB>;close(DB);
    open(DB,">$user_file"); seek(DB,0,0); print DB @userlist; close(DB);

    push(@log,"<B><FONT color=\"#ff0000\" size=\"+3\" face=\"�ͣ� ��ī\">�����⡼��</FONT></B><BR><BR>\n");
    push(@log,"�Хå����åפ��ɹ��ޤ�����<br>\n");
    push(@log,"<br><B><FONT color=\"#ff0000\">>><a href=\"$home\">HOME</a> >><a href=\"$adm\">ADMIN</a></b></FONT>\n");

    &HEADER ;
    print @log;
    &FOOTER;
}
#==================#
# �� �ǥ����ɽ���  #
#==================#
sub ADMDECODE {
    $p_flag=0;
    if ($ENV{'REQUEST_METHOD'} eq "POST") {
        if ($ENV{'CONTENT_LENGTH'} > 51200) { &ERROR("�۾�����ϤǤ�"); }
        read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
        $p_flag=1;
    } else { $buffer = $ENV{'QUERY_STRING'}; }
    @pairs = split(/&/, $buffer);
    foreach (@pairs) {
        ($name,$value) = split(/=/, $_);
        $value =~ tr/+/ /;
        $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

        # ʸ�������ɤ�EUC�Ѵ�
        if ($name eq "Del") { push(@DEL,$value);}
        &jcode'convert(*value, "euc", "", "z");
        &jcode::tr(\$value, '��', ' ');

        $value =~ s/</&lt;/g;
        $value =~ s/>/&gt;/g;
        $value =~ s/&/&amp;/g;
        $value =~ s/"/&quot;/g;
        $value =~ s/ /&nbsp;/g;
        $value =~ s/,/��/g; #�ǡ�����»�к�

        $in{$name} = $value;
    }

    $id = $in{'Id'};
    $admpass = $in{'Password'};
    $Command = $in{'Command'};
    $Message = $in{'Message'};
    if($buffer eq ""){$Command = "LOGON"; $p_flag=1;}

}
#==================#
# �� ����ɽ������  #
#==================#
sub USERLIST {

    local($col_s1) = "<font color=white>" ;
    local($col_s2) = "<font color=red>" ;
    local($col_e) = "</font>" ;
    local($hostlist) = "," ;

    push(@log,"<P align=\"center\"><B><FONT color=\"#ff0000\" size=\"+3\" face=\"�ͣ� ��ī\">��¸�԰���</FONT></B><BR></P>");
    push(@log,"<form action=\"admin.cgi\" method=\"POST\">\n");
    push(@log,"�����å�������<INPUT size=\"64\" type=\"text\" name=\"Message\" maxlength=\"64\"><BR><BR>\n");
    push(@log,"<TABLE border=\"1\">\n");
    push(@log,"<tr align=\"center\"><td nowrap>�跺</td><td nowrap>̾��</td><td nowrap>ID&PASS</td><td nowrap>���롼��</td><td nowrap>����</td><td nowrap>�Уþ���</td></tr>\n");
    foreach (0 .. $#userlist) {
        ($w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_group,$w_gpass,$w_a_name,$w_feel,$w_host,$w_os) = split(/,/, $userlist[$_]);

        if ($w_hit <= 0) {
            $col_s = $col_s2; $w_sts = "��˴";
        } else {
            $col_s = $col_s1;
            if ($w_host ne "") {
                if ($hostlist =~ /,$w_host,/) {
                    $col_s = "<font color=yellow>";
                } else {
                    $hostlist = ($hostlist . $w_host . ",");
                }
            }
        }

        push(@log,"<tr><td><input type=checkbox name=Del value=\"$_\"></td><td align=\"center\" nowrap>$col_s$w_f_name $w_l_name$col_e</td><td nowrap>$col_s$w_id<BR>$w_password$col_e</td><td nowrap>$col_s$w_group<BR>$w_gpass$col_e</td><td nowrap>$col_s$w_sts($w_tactics)<BR>$place[$w_pls]$col_e</td><td>$col_s$w_host<BR>$w_os$col_e</td></tr>\n");

    }
    push(@log,"</table><BR>\n");
    push(@log,"<input type=hidden name=Command value=\"USERDEL\">\n") ;
    push(@log,"<input type=hidden name=Password value=$admpass>\n");
    push(@log,"<input type=submit value=\"�������\"><input type=reset value=\"�ꥻ�å�\">\n") ;
    push(@log,"</form><BR>\n");

    &HEADER ;
    print @log;
    &FOOTER;

}
#==================#
# �� �������      #
#==================#
sub USERDEL {

    open(DB,"$user_file");seek(DB,0,0); @userlist=<DB>;close(DB);

    foreach (0 .. $#DEL) {
        ($w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_group,$w_gpass,$w_a_name,$w_feel,$w_host,$w_os) = split(/,/, $userlist[$DEL[$_]]);
        $w_msg = $Message;
        &LOGSAVE("DEATH4") ;
        $w_hit = 0 ; $w_sts = "��˴"; $w_death=$deth;
        $userlist[$DEL[$_]] = "$w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_group,$w_gpass,$w_a_name,$w_feel,$w_host,$w_os,\n" ;
    }

    open(DB,">$user_file"); seek(DB,0,0); print DB @userlist; close(DB);


    &USERLIST;

}
1
