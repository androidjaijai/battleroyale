#==================#
# �� ��å� ����   #
#==================#

$listmax = 300;  # ��å������ݴɿ�
$mesmax = 10;   # ����ɽ����å��������
$mes = 100;     # ����κ����å�����Ĺ

$mesall = 1;    # ��������å�������off:0 / on:1��

$col_to   = "#ff0000";  # ������å������ο�
$col_from = "#00ffff";  # ȯ����å������ο�
$col_all  = "#ffffff";  # ��������å������ο�
$col_adm  = "#ffff00";  # �����Ͱ���å������ο�
$col_grp  = "#00ff00";  # ���롼�װ���å������ο�

#==================#
# �� ��å� �ᥤ�� #
#==================#
sub MESMAIN {

    local($hitbarleng) = 0; if ($hit > 0) { $hitbarleng = int($hit / $mhit * 45); }
    local($hitbarlenr) = 45 - $hitbarleng;
    local($stabarleng) = int($sta / $maxsta * 45);
    local($stabarlenr) = 45 - $stabarleng;

    $up = ($level * $level) + ($level * $baseexp);

    $kega ="" ;
    if ($inf =~ /Ƭ/) {$kega = ($kega . "Ƭ����") ;}
    if ($inf =~ /��/) {$kega = ($kega . "�ӡ�") ;}
    if ($inf =~ /ʢ/) {$kega = ($kega . "ʢ����") ;}
    if ($inf =~ /­/) {$kega = ($kega . "­��") ;}
    if ($inf =~ /��/) {$kega = ($kega . "�ǡ�") ;}
    if ($inf =~ /��/) {$kega = ($kega . "������") ;}
    if ($kega eq "") { $kega = "��" ;}

    local($w_name,$w_kind) = split(/<>/, $wep);
    if (($we eq "B") && ($w_kind =~ /B/)) { $tactics2 = "��"; }
    elsif (($we eq "P") && ($w_kind =~ /P/)) { $tactics2 = "��"; }
    elsif (($we eq "A") && ($w_kind =~ /A/) && ($wtai > 0)) { $tactics2 = "��"; }
    elsif (($we eq "G") && ($w_kind =~ /G/) && ($wtai > 0)) { $tactics2 = "��"; }
    elsif (($we eq "N") && ($w_kind =~ /N/)) { $tactics2 = "��"; }
    elsif (($we eq "S") && ($w_kind =~ /S/)) { $tactics2 = "��"; }
    elsif (($we eq "D") && ($w_kind =~ /D/)) { $tactics2 = "��"; }
    elsif (($we eq "C") && ($w_kind =~ /C/)) { $tactics2 = "��"; }
    else { $tactics2 = "����̵��"; }

    local($tension);
    if($feel == 300) {
        $tension = "<font color=\"red\">Ķ��</font>";
    }elsif($feel > 240) {
        $tension = "<font color=\"orange\">Ķ����</font>";
    }elsif($feel > 180) {
        $tension = "<font color=\"yellow\">����</font>";
    }elsif($feel > 120) {
        $tension = "<font color=\"lime\">����</font>";
    }elsif($feel > 60) {
        $tension = "<font color=\"aqua\">�嵤</font>";
    }elsif($feel > 0) {
        $tension = "<font color=\"blue\">ݵ</font>";
    }else{
        $tension = "<font color=\"fuchsia\">����</font>";
    }

    $nowtime = sprintf("%04dǯ%02d��%02d����%s��%02d:%02d:%02d",$year, $month, $mday, ('��','��','��','��','��','��','��') [$wday], $hour, $min, $sec);

    open(DB,"$MES_DIR/$mes_file");seek(DB,0,0); @mes_list=<DB>;close(DB);

    $chkmes ="OFF"; $mes_i = 0;
    foreach (0 .. $#mes_list) {
        ($to,$from,$message,$mestime) = split(/,/, $mes_list[$_]);
        ($how,$to_id) = split(/_/, $to);
        if ($how eq "id") {
            #����
            if ($id eq $to_id) {
                $chkmes ="ON";
                push(@log,"<font color=\"$col_to\">$message</font> [$mestime]<br>\n");
                if ($mesmax <= $mes_i++) { last; }
            #����
            } elsif ($id eq $from) {
                $chkmes ="ON";
                push(@log,"<font color=\"$col_from\">$message</font> [$mestime]<br>\n");
                if ($mesmax <= $mes_i++) { last; }
            }
        #���롼��
        } elsif (($how eq "group") && ($group eq $to_id)) {
            $chkmes ="ON";
            push(@log,"<font color=\"$col_grp\">$message</font> [$mestime]<br>\n");
            if ($mesmax <= $mes_i++) { last; }
        #������
        } elsif (($how eq "admin") && (($id eq $from) || ($id eq "kiri1120") || ($id eq "adminid0"))) {
            $chkmes ="ON";
            push(@log,"<font color=\"$col_adm\">$message</font> [$mestime]<br>\n");
            if ($mesmax <= $mes_i++) { last; }
        #���̣�
        } elsif ($how eq "ALL") {
            $chkmes ="ON";
            push(@log,"<font color=\"$col_all\">$message</font> [$mestime]<br>\n");
            if ($mesmax <= $mes_i++) { last; }
        }
    }

    if ($chkmes eq "OFF") { push(@log,"<br><center><b>��å������Ϥ���ޤ���</b></center>\n"); }

print <<"_HERE_";
<TABLE width="610">
  <TBODY>
    <TR>
      <TD align="center" colspan="2"><B><FONT color="#ff0000" size="+3" face="�ͣ� ��ī">�£ҥ�å��󥸥㡼</FONT></B></TD>
    </TR>
    <TR>
      <TD align="center" colspan="2"><B><FONT color="#ff0000">@links</FONT></B></TD>
    </TR>
    <TR>
      <TD valign="top" width="400" height="311">
      <TABLE border="1" width="400" cellspacing="0" height="310">
        <TBODY>
          <TR>
            <TH colspan="5">$nowtime</TH>
          </TR>
          <TR>
            <TD ROWSPAN="4" width="17%" nowrap><IMG src="$imgurl$icon" width="70" height="70" border="0" align="middle"></TD>
            <TH width="16%" nowrap>�� ̾</TH><TD nowrap colspan="3">$f_name $l_name ($cl $sex$no��)</TD>
          </TR>
          <TR>
            <TH nowrap>�� ��</TH><TD nowrap>$club</TD>
            <TH nowrap>����</TH><TD nowrap>$a_name</TD>
          </TR>
          <TR>
            <TH nowrap>�� ��</TH><TD nowrap><img src="$imgurl$bar_green" width=$hitbarleng height=10><img src="$imgurl$bar_red" width=$hitbarlenr height=10> $hit/$mhit</TD>
            <TH width="16%" nowrap>��٥�</TH><TD width="16%" nowrap>$level($exp/$up)</TD>
          </TR>
          <TR>
            <TH nowrap>�����ߥ�</TH><TD nowrap><img src="$imgurl$bar_green" width=$stabarleng height=10><img src="$imgurl$bar_red" width=$stabarlenr height=10> $sta/$maxsta</TD>
            <TH nowrap>�ƥ󥷥��</TH><TD nowrap>$tension</TD>
          </TR>
          <TR>
            <TH nowrap>����Ľ�</TH><TD nowrap colspan="2">$kega</TD>
            <TH nowrap>����</TH><TD nowrap><font color="red"><b>$kill</b></font>�ͻ���</TD>
          </TR>
          <TR>
            <TH nowrap>����</TH><TD nowrap colspan="2">$tactics(ȿ�⡧$tactics2)</TD>
            <TH nowrap>����</TH><TD nowrap>$sts</TD>
          </TR>
          <TR>
            <TH nowrap>���롼��</TH><TD nowrap colspan="4">$group($gpass)</TD>
          </TR>
          <TR height="210">
            <TD colspan="5" valign="top">
              <TABLE width="400" height="180">
                <TR align="center">
                  <TD width="20%" nowrap><B>ɽ��ʸ����</B></TD>
                  <TD nowrap>
<font color="$col_to">����</font>��
<font color="$col_from">ȯ��</font>��
<font color="$col_all">�����ؤ�ȯ��</font>��
<font color="$col_grp">���롼�װ�</font>��
<font color="$col_adm">�����Ͱ�</font>��
                  </TD>
                </TR>
                <TR height="170">
                  <TD valign="top" colspan="2">
@log
                  </TD>
                </TR>
                <TR>
                  <TD colspan="2" nowrap align="right" valign="bottom"><B>Base script:<A href="http://kurisutof.hp.infoseek.co.jp/" target="_blank">�£ҥ�å��󥸥㡼Ver1.03</A></B></TD>
                </TR>
              </TABLE>
            </TD>
          </TR>
        </TABLE>
      </TD>
      <TD valign="top" width="210" height="346">
      <TABLE border="1" cellspacing="0" height="346">
        <TBODY>
          <TR><TH width="210">���ޥ��</TH>
          <TR>
            <TD align="left" valign="top" width="210" height="335">
            <FORM METHOD="POST" name="f1">
            <INPUT TYPE="HIDDEN" NAME="mode" VALUE="command">
            <INPUT TYPE="HIDDEN" NAME="Id" VALUE="$id2">
            <INPUT TYPE="HIDDEN" NAME="Password" VALUE="$password2">
_HERE_

        print "ï�˥�å�����������ޤ�����<BR><BR>\n";
        print "��<select name=\"Command\">\n" ;
        print "<option value=\"MAIN\" selected>���</option>\n";
        if ($sts eq "����") {
            print "<option value=\"HEAL2\">����</option>\n";
        } elsif ($sts eq "��̲") {
            print "<option value=\"INN2\">��̲</option>\n";
        } elsif ($sts eq "�ٷ�") {
            print "<option value=\"KYUKEI2\">�ٷ�</option>\n";
        }
        print "<option value=\"SENDMES_reload\">�����</option>\n";
        for ($k=0; $k<=$#userlist; $k++) {
            ($w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_group,$w_gpass,$w_a_name,$w_feel,$w_host,$w_os) = split(/,/, $userlist[$k]);
            if (($id ne $w_id) && (($gpass eq $w_gpass) || ($gpass eq $w_gpass) || ($id eq "kiri1120") || ($id eq "adminid0")) && ($w_hit > 0) && ($w_inf !~ /NPC/)) {
                print "<option value=\"SENDMES_id_$w_id\_$k\">$w_f_name $w_l_name</option>\n";
            }
        }
        print "<option value=\"SENDMES_group_$group\">���롼������</option>\n";
        print "<option value=\"SENDMES_ALL\">���ü�����</option>\n";
        print "<option value=\"SENDMES_admin\">������</option>\n";
        print "</select><BR>\n" ;
        print "<BR>\n";
        print "��å����������Ϥ��Ƥ���������<BR>������", $mes / 2, "ʸ���ޤǡ�<BR><BR>\n";
        print "��<INPUT size=\"30\" type=\"text\" name=\"speech\" maxlength=\"$mes\"><BR><BR>\n";
        print "��<INPUT type=\"submit\" name=\"Enter\" value=\"����\" ondblclick=\"dbk()\">\n";

print <<"_HERE_";
            </FORM>
            </TD>
          </TR>
        </TBODY>
      </TABLE>
      </TD>
    </TR>
    <TR>
      <TD valign="top" height="151">
      <TABLE border="1" cellspacing="0" height="150" cellpadding="0" width="410">
        <TBODY>
          <TR>
            <TH height="10">��������ɥ�</TH>
          </TR>
          <TR>
            <TD height="140" valign="top">$log</TD>
          </TR>
        </TBODY>
      </TABLE>
      </TD>
      <TD valign="top" height="151">
      <TABLE border="1" cellspacing="0" height="150" cellpadding="0">
        <TBODY>
          <TR>
            <TH height="10" width="210" nowrap>���롼�ץ��С�</TH>
          </TR>
          <TR>
            <TD height="140" valign="top" width="210" nowrap>
_HERE_

            &GrpMem;

print <<"_HERE_";
            </TD>
          </TR>
        </TBODY>
      </TABLE>
      </TD>
    </TR>
  </TBODY>
</TABLE>
_HERE_

$mflg="ON"; #���ơ�������ɽ��
}

#==================#
# �� ��å� ����   #
#==================#
sub SENDMES {

    local($a,$how,$mes_id,$k) = split(/_/, $Command);


    if (length($speech) > $mes) {
        $log = ($log . "��å�����������ʸ����������" . $mes / 2 . "ʸ���ˤ�ۤ��Ƥ��ޤ���<BR>");
    } elsif (($speech ne "") && ($how ne "reload")) {
        $to = "";
        if ($how eq "id") {
            ($w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_group,$w_gpass,$w_a_name,$w_feel,$w_host,$w_os) = split(/,/, $userlist[$k]);
            if (($w_id eq $mes_id) && ($w_id ne $id) && ($w_hit > 0) && ($w_inf !~ /NPC/)) {
                $to = "��$w_f_name $w_l_name";
                $mes_id = "_" . $w_id;
            }
            if ($to eq "") { &ERROR("�����ʥ��������Ǥ���"); }
        }
        elsif ($how eq "group") { $to = "��$group"; $mes_id = "_" . $group; }
        elsif ($how eq "admin") { $to = "�������"; $mes_id = ""; }
        elsif ($how eq "ALL") {   $to = ""; $mes_id = ""; }
        else { &ERROR("�����ʥ��������Ǥ���"); }

        open(IN,"$MES_DIR/$mes_file");seek(IN,0,0); @meslist=<IN>;close(IN);

        local($nowtime) = sprintf("%02d/%02d (%02d:%02d)", $month, $mday, $hour, $min);
        $message = "$how$mes_id,$id,$f_name $l_name��$speech$to,$nowtime,\n";
        unshift (@meslist, $message);
        if ($#meslist >= $listmax) { pop (@meslist); }

        open(OUT,">$MES_DIR/$mes_file"); seek(OUT,0,0); print OUT @meslist; close(OUT);

        $log = ($log . "��å��������������ޤ�����<BR>");

    }

    &SAVE;

    &HEADER;
    &MESMAIN;
    &FOOTER;
}
1;
