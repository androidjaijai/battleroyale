#!/usr/bin/perl
require "jcode.pl";
require "br.cgi";
require "$LIB_DIR/lib.cgi";
require "$LIB_DIR/lib2.cgi";
&LOCK;
require "pref.cgi";

&DECODE;
&CREAD ;

# �ǡ��������������ӽ�
if ($d_ricovor) { &ERROR("�ǡ������ƥʥ���Ǥ�������äȤ������Ԥ���������"); }

if ($mode eq "regist") { &REGIST; }
elsif ($mode eq "info") { &INFO; }
elsif ($mode eq "info2") { &INFO2; }
elsif ($mode eq "icon") { &ICON; }
else { &MAIN; }
&UNLOCK;
exit;

#==================#
# �� �ᥤ��        #
#==================#
sub MAIN {

&Checker;

&HEADER;
print <<"_HERE_";
<P align="center"><B><FONT color=\"#ff0000\" size=\"+3\" face=\"�ͣ� ��ī\">ž����³��</FONT></B><BR><BR>
<BR>
<img src="$imgurl$n_icon_file[$#n_icon_file]"><BR><BR>
�ط���ž�������͡��ͤ�ôǤ�Ǥ���<BR>
���̤���ϡ��֤Ȥ�ܡפȤ������Ƥ뤱�ɤ͡�<BR>
��������ʻ��Ϥɤ��Ǥ⤤���͡�<BR>
<BR>
�Ȥꤢ�����������˻�̾�ȡ����̤������ơ�<BR>
��Ф��Ƥ�館�뤫�ʡ�</P>
<CENTER>
<FORM METHOD="POST">
<INPUT TYPE="HIDDEN" NAME="mode" VALUE="regist">
����<INPUT size="16" type="text" name="F_Name" maxlength="16"><BR>
̾��<INPUT size="16" type="text" name="L_Name" maxlength="16"><BR>
���Ρ�<INPUT size="16" type="text" name="A_Name" maxlength="16"><BR>
<BR>
���̡�<SELECT name="Sex">
  <OPTION value="NOSEX" selected>- ���� -</OPTION>
  <OPTION value="�˻�">�˻�</OPTION>
  <OPTION value="����">����</OPTION>
</SELECT>
_HERE_

    print "����������<SELECT name=\"Icon\">\n";
    print "<OPTION value=\"NOICON\" selected>- �������� -</OPTION>\n";
    for ($i=0;$i<$icon_check3;$i++){
            print "<OPTION value=\"$i\">$icon_name[$i]</OPTION>\n";
    }
    print "</SELECT>\n";

print <<"_HERE_";
<BR><a href="regist.cgi?mode=icon" target="_brank">�����������</a>
<BR><BR>
ID��<INPUT size="8" type="text" name="Id" maxlength="8">���ѥ���ɡ�<INPUT size="8" type="text" name="Password" maxlength="8"><BR>
��ID,�ѥ���ɤ�Ⱦ�ѱѿ���8ʸ�������<BR>
<BR>
���롼��̾��<INPUT size="10" type="text" name="Group" maxlength="20">�����롼�ץѥ���<INPUT size="10" type="text" name="Gpass" maxlength="20"><BR>
������10ʸ������ǥ��롼�פ����äƤ��ʤ��ͤ����Ϥ��Ƥ�����������<BR>
<BR>
���ʡ�<INPUT size="32" type="text" name="Message" maxlength="64"><BR>
����껦��������졣���ѣ���ʸ���ޤǡ�<BR>
�����<INPUT size="32" type="text" name="Message2" maxlength="64"><BR>
�ʼ�ʬ��˴��������<BR>
���ʥ��ԡ��롧<INPUT size="32" type="text" name="Comment" maxlength="64"><BR>
�ʰ�������ȡ���¸�԰����˵��ܤ���롣��<BR>
<BR>
<FONT color="#ffff00" size="+1"><B>
Ʊ��ץ쥤�䡼��ʣ����Ͽ��������������Ѥ�<BR>
»�ʤ�̾������Ͽ�Ϥ���θ����������<BR>
���㡧����̾����̾��Ƚ�ǽ���ʤ�̾�������̤Ȱ㤦̾���������̾����<BR>
�����ͤΰ�¸�ǥǡ�������������ޤ���<BR>
<BR>
�ޤ���<a href="rule.htm" target="_blank">������</a>�Ϥ�������ɤ�Ǥ���������<BR>
����������ɤ�Ǥ��ʤ��ä�����פȤ����Τϡ���ȿ�԰٤���������ͳ�ˤϤʤ�ޤ���<BR>
</B></FONT>
<BR>
<INPUT type="submit" name="Enter" value="�� ��"> ��<INPUT type="reset" name="Reset" value="�ꥻ�å�"><BR>
</FORM>
</CENTER>
<P align="center"><A href="$home"><B><FONT color="#ff0000" size="+2">���</FONT></B></A></P>
_HERE_

&FOOTER;

}
#==================#
# �� ��Ͽ����      #
#==================#
sub REGIST {

&Checker;

    #���Ͼ�������å�
    if ($f_name2 eq '') { &ERROR("����̤���ϤǤ���") ; }
    elsif (length($f_name2) > 8) { &ERROR("����ʸ�����������С����Ƥ��ޤ��������ѣ�ʸ���ޤǡ�") ; }
    elsif ($f_name2 =~ /\w/) { &ERROR("��̾��Ⱦ��ʸ�������ѤǤ��ޤ���") ; }

    elsif ($l_name2 eq '') { &ERROR("̾��̤���ϤǤ���") ; }
    elsif (length($l_name2) > 8) { &ERROR("̾��ʸ�����������С����Ƥ��ޤ��������ѣ�ʸ���ޤǡ�") ; }
    elsif ($l_name2 =~ /\w/) { &ERROR("��̾��Ⱦ��ʸ�������ѤǤ��ޤ���") ; }

    elsif (length($id2) > 8) { &ERROR("ID��ʸ�����������С����Ƥ��ޤ�����Ⱦ��8ʸ���ޤǡ�") ; }
    elsif ($id2 eq '') { &ERROR("ID��̤���ϤǤ���") ; }
    elsif ($id2 =~ /\W/) { &ERROR("ID��Ⱦ�Ѥ����Ϥ��Ƥ�����������Ⱦ�ѣ�ʸ���ޤǡ�") ; }
    elsif ($id2 =~ /\_|\,|\;|\<|\>|\(|\)|&|\/|\./) { &ERROR("ID�˻��Ѷػ�ʸ�������äƤ��ޤ���") ; }

    elsif ($password2 eq '') { &ERROR("�ѥ���ɤ�̤���ϤǤ���") ; }
    elsif (length($password2) > 8) { &ERROR("�ѥ���ɤ�ʸ�����������С����Ƥ��ޤ�����Ⱦ�ѣ�ʸ���ޤǡ�") ; }
    elsif ($password2 =~ /\W/) { &ERROR("�ѥ���ɤ�Ⱦ�Ѥ����Ϥ��Ƥ�����������Ⱦ�ѣ�ʸ���ޤǡ�") ; }
    elsif ($password2 =~ /\_|\,|\;|\<|\>|\(|\)|&|\/|\./) { &ERROR("�ѥ���ɤ˻��Ѷػ�ʸ�������äƤ��ޤ���") ; }

    elsif ($group2 eq '') { &ERROR("���롼��̾��̤���ϤǤ���") ; }
    elsif (length($group2) > 20) { &ERROR("���롼��̾��ʸ�����������С����Ƥ��ޤ��������ѣ�ʸ���ޤǡ�") ; }
    elsif ($group2 =~ /^(\x81\x40|\s|&nbsp;)+$/) { &error("���롼��̾���������������Ƥ�������"); }
    elsif ($gpass2 eq '') { &ERROR("���롼�ץѥ���̤���ϤǤ���") ; }
    elsif (length($gpass2) > 20) { &ERROR("���롼�ץѥ���ʸ�����������С����Ƥ��ޤ��������ѣ�ʸ���ޤǡ�") ; }
    elsif ($gpass2 =~ /^(\x81\x40|\s|&nbsp;)+$/) { &error("���롼�ץѥ����������������Ƥ�������"); }

    elsif ($sex2 eq "NOSEX") { &ERROR("���̤�̤����Ǥ���") ; }
    elsif ($icon2 eq "NOICON") { &ERROR("��������̤����Ǥ���") ; }
    elsif ($id2 eq $password2) { &ERROR("ID��Ʊ��ʸ����ϥѥ���ɤ˻Ȥ��ޤ���") ; }
    elsif (length($msg2) > 64) { &ERROR("���ʤ�ʸ�����������С����Ƥ��ޤ��������ѣ���ʸ���ޤǡ�") ; }
    elsif (length($dmes2) > 64) { &ERROR("�����ʸ�����������С����Ƥ��ޤ��������ѣ���ʸ���ޤǡ�") ; }
    elsif (length($com2) > 64) { &ERROR("�����Ȥ�ʸ�����������С����Ƥ��ޤ��������ѣ���ʸ���ޤǡ�") ; }
    elsif (($icon2 >= $icon_check2)&&($password2 ne $s_icon_pass[$icon2 - $icon_check2])) { &ERROR("���Υ��������$icon_name[$icon2]�Ǥ���") ; }
    elsif ($icon2 < $icon_check2){
        if(($sex2 =~ /�˻�/)&&($icon2 >= $icon_check )) { &ERROR("���̤Ȱ㤦������������򤷤Ƥ��ޤ���") ; }
        elsif(($sex2 =~ /����/)&&($icon2 < $icon_check )){ &ERROR("���̤Ȱ㤦������������򤷤Ƥ��ޤ���") ; }
    }

    #Ʊ��Ʊ̾���ɣĥ����å�
    $grpmem = $gpsmem = 0;
    foreach $userlist(@userlist) {
        ($w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_group,$w_gpass,$w_a_name,$w_feel,$w_host,$w_os) = split(/,/, $userlist);
        if (($id2 eq $w_id) || (($f_name2 eq $w_f_name)&&($l_name2 eq $w_l_name)&&($w_sts ne "��˴"))) {    #Ʊ��ID or Ʊ��Ʊ̾?
            &ERROR("Ʊ��ɣġ��㤷���ϡ�Ʊ��Ʊ̾�Υ���饯��������¸�ߤ��ޤ���") ;
        }
        if ($group2 eq $w_group) {
            $grpmem++;
            if ($grpmem >= 6) { &ERROR("Ʊ�쥰�롼�ףɣĤϣ��ͤޤǤǤ���") ; }
        }
        if ($gpass2 eq $w_gpass) {
            $gpsmem++;
            if ($gpsmem >= 6) { &ERROR("Ʊ�쥰�롼�ץѥ��ϣ��ͤޤǤǤ���") ; }
        }
    }

    #�ٵ����ե�����
    open(DB,"$wep_file") || exit; seek(DB,0,0); @weplist=<DB>; close(DB);

    #��ʪ�ե�����
    open(DB,"$stitem_file") || exit; seek(DB,0,0); @stitemlist=<DB>; close(DB);

    #�����ֹ�ե�����
    open(DB,"$member_file") || exit; seek(DB,0,0); $memberlist=<DB>; close(DB);
    ($m,$f,$mc,$fc) = split(/,/, $memberlist);

    #���̿Ϳ������å�
    if ($sex2 eq "�˻�") {
        if ($mc >= $clmax) { #��Ͽ�Բ�ǽ��
            &ERROR("�˻����̤Ϥ���ʾ���Ͽ�Ǥ��ޤ���") ;
        }
        $m+=1;$no=$m;$cl=$clas[$mc];
        if ($m >= $manmax) {    #���饹������
            $m=0;$mc+=1;
        }
    } else {
        if ($fc >= $clmax) { #��Ͽ�Բ�ǽ��
            &ERROR("�������̤Ϥ���ʾ���Ͽ�Ǥ��ޤ���") ;
        }
        $f+=1;$no=$f;$cl=$clas[$fc];
        if ($f >= $manmax) {    #���饹������
            $f=0;$fc+=1;
        }
    }

    #�����ֹ�ե����빹��
    $memberlist="$m,$f,$mc,$fc,\n" ;
    open(DB,">$member_file"); seek(DB,0,0); print DB $memberlist; close(DB);

    #����������ꥹ�ȼ���
    $index = int(rand($#weplist+1));
    ($w_wep,$w_att,$w_tai) = split(/,/, $weplist[$index]);

    #��ʪ�����ƥ�ꥹ�ȼ���
    $index = int(rand($#stitemlist+1));
    local($st_item,$st_eff,$st_tai) = split(/,/, $stitemlist[$index]);

    #����ʽ����
    for ($i=0; $i<6; $i++) {
        $item[$i] = "�ʤ�"; $eff[$i]=$itai[$i]=0;
    }

    #���ǽ��
    $att = int(rand(5)) + 8 ;
    $def = int(rand(5)) + 8 ;
    $hit = int(rand(20)) + 90 ;
    $mhit = $hit ;
    $kill = 0;
    $sta = 100;
    $level = 1; $exp = 0;
    $death = $msg = "";
    $sts = "����"; $pls = 0;
    $tactics = "�̾�" ;
    $endtime = 0 ;
    $log = "";
    $dmes = "" ; $bid = "" ; $wf=""; $inf = "" ;
    $we = "";
    $feel = int(rand(20)) + 120;
    $icon2 = $icon_file[$icon2];

    #��������ƥ������������
    $item[0] = "�ѥ�<>SH"; $eff[0] = 50; $itai[0] = 2;
    $item[1] = "��<>HH"; $eff[1] = 20; $itai[1] = 2;
    $item[2] = $w_wep; $eff[2] = $w_att; $itai[2] = $w_tai;

    $wep = "�Ǽ�<>WP";
    $watt = 0;
    $wtai = "��" ;

    if ($sex2 eq "�˻�" ) {
        $bou = "�إ��<>DBN";
    } else {
        $bou = "�����顼��<>DBN";
    }
    $bdef = 5;
    $btai = 30;

    $bou_h = $bou_f = $bou_a = "�ʤ�" ;
    $bdef_h = $bdef_f = $bdef_a = 0;
    $btai_h = $btai_f = $btai_a = 0 ;

    #��������ٵ�
    if ($w_wep =~ /<>WG/) { #��
        $item[3] = "�ƴ�<>Y"; $eff[3] = 36; $itai[3] = 1;
        $item[4] = $st_item; $eff[4] = $st_eff; $itai[4] = $st_tai;
    } elsif ($w_wep =~ /<>WA/) {    #��
        $item[3] = "��<>Y"; $eff[3] = 36; $itai[3] = 1;
        $item[4] = $st_item; $eff[4] = $st_eff; $itai[4] = $st_tai;
    } else {
        $item[3] = $st_item; $eff[3] = $st_eff; $itai[3] = $st_tai;
    }

    &CLUBMAKE ; #����ֺ���

    #�����桼�������Ǽ
    $newuser = "$id2,$password2,$f_name2,$l_name2,$sex2,$cl,$no,$endtime,$att,$def,$hit,$mhit,$level,$exp,$sta,$wep,$watt,$wtai,$bou,$bdef,$btai,$bou_h,$bdef_h,$btai_h,$bou_f,$bdef_f,$btai_f,$bou_a,$bdef_a,$btai_a,$tactics,$death,$msg2,$sts,$pls,$kill,$icon2,$item[0],$eff[0],$itai[0],$item[1],$eff[1],$itai[1],$item[2],$eff[2],$itai[2],$item[3],$eff[3],$itai[3],$item[4],$eff[4],$itai[4],$item[5],$eff[5],$itai[5],$log,$dmes2,$bid,$club,$wn,$wp,$wa,$wg,$we,$wc,$wd,$wb,$wf,$ws,$com2,$inf,$group2,$gpass2,$a_name2,$feel,$host,$os,\n" ;
    open(DB,">>$user_file"); seek(DB,0,0); print DB $newuser; close(DB);

    #�����ɲå�
    &LOGSAVE("NEWENT") ;

    $id=$id2; $password=$password2;

    &CSAVE ;    #���å�����¸

&HEADER;

print <<"_HERE_";
<P align="center"><B><FONT color="#ff0000" size="+3" face="�ͣ� ��ī">ž����³����λ</FONT></B><BR></P>
<TABLE border="1" width="280" cellspacing="0">
  <TBODY>
    <TR>
      <TD width="60">���饹</TD>
      <TD colspan="3" width="113">$cl</TD>
    </TR>
    <TR>
      <TD>��̾</TD>
      <TD colspan="3">$f_name2 $l_name2</TD>
    </TR>
    <TR>
      <TD>�ֹ�</TD>
      <TD colspan="3">$sex2$no��</TD>
    </TR>
    <TR>
      <TD>�����</TD>
      <TD colspan="3">$club</TD>
    </TR>
    <TR>
      <TD>����</TD>
      <TD>$hit/$mhit</TD>
      <TD>�����ߥ�</TD>
      <TD>$sta</TD>
    </TR>
    <TR>
      <TD>������</TD>
      <TD>$att</TD>
      <TD>���</TD>
      <TD>��</TD>
    </TR>
    <TR>
      <TD>�ɸ���</TD>
      <TD>$def</TD>
      <TD>�ɶ�</TD>
      <TD>��</TD>
    </TR>
  </TBODY>
</TABLE>
<P align="center"><BR>
<img src="$imgurl$n_icon_file[$#n_icon_file]"><BR>
_HERE_

    if ($sex2 eq "�˻�") {
        print "$f_name2 $l_name2������͡�<BR>\n" ;
    } else {
        print "$f_name2 $l_name2������͡�<BR>\n" ;
    }

print <<"_HERE_";

ž���᡹�����ɡ������Ͻ���ι�Ԥ���<BR>
<BR>
��������٤줺�ˤ���������<BR><BR>
<FORM METHOD="POST"  ACTION="regist.cgi">
<INPUT TYPE="HIDDEN" NAME="mode" VALUE="info">
<INPUT TYPE="HIDDEN" NAME="Id" VALUE="$id2">
<INPUT TYPE="HIDDEN" NAME="Password" VALUE="$password2">
<center>
<INPUT type="submit" name="Enter" value="����ι�Ԥؽ�ȯ">
</center>
</FORM>
</P>
_HERE_
&FOOTER;
}

#==================#
# �� ��������      #
#==================#
sub INFO {

&HEADER;

print <<"_HERE_";
<P align="center"><B><FONT color="#ff0000" size="+3" face="�ͣ� ��ī">��Ͽ��λ</FONT></B><BR><BR>
�ܤ������ȡ������Τ褦�ʽ�ˤ���������ι�Ԥ˹Ԥä��Ϥ��ʤΤˡ�������<BR>
�֤�����������ι�Ԥ˹Ԥ��Х�����ǵޤ�̲�������äƤ��ơ�������<BR>
������Ϥ��ȡ�¾�����̤⤤��褦�����褯����ȡ������俧�μ��ؤ��Ϥ���Ƥ�����˵��Ť���<BR>
��ʬ�μ�˿����ȡ��䤿����°�δ���������äƤ�����<BR>
����Ʊ�͡����ζ俧�μ��ؤ��Ϥ���Ƥ�����<BR>
<BR>
�����������⤫�顢��ͤ��ˤ����äƤ�����������<BR><BR>
<BR>
<img src="$imgurl$n_icon_file[0]"><BR><BR>
�ؤ��㡢�������ޡ������ߤ�ʤˤ�������Ƥ��ä��Τ�¾�Ǥ⤢��ޤ�����<BR>
�����ϡ�������ˤ���äȡ������礤�򤷤Ƥ�餤�ޡ�����<BR>
<BR>
�դ�ä��ꡢ���μ��ؤ�Ϥ������ꡢæ�����褦�Ȼ�ߤ�����¨�¤˻������ȻפäƤ���������<BR>
<BR>
������ϡ���ǯ�Ρȥץ������оݥ��饹�����Ф�ޤ�����<BR>
<BR>
�롼��ϴ�ñ�Ǥ������ߤ����������äƤ����Ф��������Ǥ���<BR>
ȿ§�Ϥ���ޤ�����<BR><BR>
��������������˺��Ƥ����ɡ���������ǡ�����<BR>
<BR>
���������������Ϥ������ʬ���Ǥ���<BR>
�����������ˤ��äȤ��뤫��ʡ����ߤ�ʤ���Ф�Ρ�����äƤ뤫��ʡ���<BR>
<BR>
���ơ������Ǥ�������������Ф���ɤ��عԤäƤ⹽\���ޤ���<BR>
���ɡ���������ˡ����������򤷤ޤ����������ʡ���<BR>
<BR>
�����ǡ��ߤ�ʤ���äƤ��Ͽޤ˽��äơ��������餳�Υ��ꥢ�ϴ�ʤ�������<BR>
�ä������Τ餻�ޤ���<BR>
�Ͽޤ��ɤ����ơ����Ф��Ϸ���Ȥ餷��碌�ơ�<BR>
®�䤫�ˤ��Υ��ꥢ��ФƤ���������<BR>
<BR>
�ʤ�Ǥ��Ȥ����ȡ������μ��ؤϤ�äѤ���ȯ���ޤ���<BR>
<BR>
�������������餡����ʪ����ˤ��Ƥ�����������<BR>
�귡�äƱ���Ƥ����Ȥ��Ϥ��ޡ�����<BR>
���������������Ĥ��ǤǤ���������ʪ����˱����ΤϾ���ǡ�����<BR>
<BR>
����������Ȥ⤦��ġ��������ߥåȤ�����ޤ���<BR>
�����Ǥ������������ߥåȤǡ�����<BR>
<BR>
�ץ����Ǥϡ��ɤ�ɤ�ͤ���ˤޤ�������24���֤��Ϥäƻ����ͤ�ï��Ǥʤ��ä��餡��<BR>
���줬�����ڤ�ǡ��������Ȳ��ͻĤäƤ��褦�ȡ�����ԥ塼������ư���ơ�<BR>
�ĤäƤ�������μ��ؤ���ȯ���ޡ�����ͥ���ԤϤ���ޤ�����<BR>
<BR>
�����ơ����줸���ͤŤġ����Υǥ��ѥå�����äơ�������ǤƤ�餤�ޡ�������<BR>
<BR>
<FORM METHOD="POST"  ACTION="battle.cgi">
<INPUT TYPE="HIDDEN" NAME="mode" VALUE="main">
<INPUT TYPE="HIDDEN" NAME="Id" VALUE="$id2">
<INPUT TYPE="HIDDEN" NAME="Password" VALUE="$password2">
<center>
<INPUT type="submit" name="Enter" value="������Ф�">
</center>
</FORM>
_HERE_

&FOOTER;

}

#==================#
# �� ����ֺ���    #
#==================#
sub CLUBMAKE {

    $wa = $wg = $wc = $wd = $ws = $wn = $wb = $wp = 0;

    local($dice) =  rand(100) ;
    local($dice2) = int(rand(8)) ;
    local($dice3) = int(rand(8)) ;

    if ($dice < 80) {
        if ($dice2 == 0) {
            $club = "��ƻ��";
            $wa = 2 * $BASE;
        } elsif ($dice2 == 1) {
            $club = "�ͷ���";
            $wg = 2 * $BASE;
        } elsif ($dice2 == 2) {
            $club = "������";
            $wb = 2 * $BASE;
        } elsif ($dice2 == 3) {
            $club = "�Х�����";
            $wc = 2 * $BASE;
        } elsif ($dice2 == 4) {
            $club = "�ʳ���";
            $wd = 2 * $BASE;
        } elsif ($dice2 == 5) {
            $club = "�ե��󥷥���";
            $ws = 2 * $BASE;
        } elsif ($dice2 == 6) {
            $club = "��ƻ��";
            $wn = 2 * $BASE;
        } else {
            $club = "�ܥ�������";
            $wp = 2 * $BASE;
        }
    } else {
        if ($dice3 == 0) {
            $club = "Φ����" ;
            $bou_f = "Φ���ѥ��塼��<>DF" ; $bdef_f = 5; $btai_f = 15;
        } elsif ($dice3 == 1) {
            $club = "����������" ;
            $item[5] = "���ץ��<>AD" ; $eff[5] = 4; $itai[5] = 10;
        } elsif ($dice3 == 2) {
            $club = "�ѥ�������" ;
            $wep = "�ե�åԡ��ǥ�����<>WC"; $watt = 3; $wtai = 10;
        } elsif ($dice3 == 3) {
            $club = "�ݷ�Ѱ�" ;
            $wep = "��ʹ�<>WS"; $watt = 3; $wtai = "��";
        } elsif ($dice3 == 4) {
            $club = "���Х��Х���" ;
            $item[5] = "�Ͽ�<>Y" ; $eff[5] = 1; $itai[5] = 1;
        } elsif ($dice3 == 5) {
            $club = "������" ;
            $mhit += 30;
            $hit = $mhit;
            $bou = "Ĺ���<>DBN"; $bdef = 5; $btai = 50;
        } elsif ($dice3 == 6) {
            $club = "ŷ��" ;
            $wa = $wg = $wc = $wd = $ws = $wn = $wb = $wp = 2 * $BASE;
        } else {
            $club = "�����" ;
            $def += int(rand(3)+2);
            $item[5] = "��ྮƻ��<>ADB" ; $eff[5] = 3; $itai[5] = 10;
        }
    }

}

#==================#
# �� ��ʣ�����å�  #
#==================#
sub Checker {

    if(($limit == "")||($limit == 0)){ $limit = 7; }
    local($t_limit) = ($limit * 3) + 1;

    if (($fl =~ /��λ/)||($ar >= $t_limit)){
        &ERROR("�ץ����μ��դϽ�λ�������ޤ�����<br><br>������ץ���೫�Ϥ��Ԥ���������") ;
    }


    $chktim = $c_endtime + (1*60*60*2) ;    #��˴���ּ���
    ($csec,$cmin,$chour,$cmday,$cmonth,$cyear,$cwday,$cyday,$cisdst) = localtime($chktim);
    $cyear+=1900; $cmonth++;

    if ($chktim > $now) {   #��Ͽ���֥��顼��
        &ERROR("������˴��ǧ�塢�����֤Ϻ���Ͽ����ޤ���<br><br>��������Ͽ��ǽ\���֡�$cyear/$cmonth/$cmday $chour:$cmin:$csec") ;
    }

    #�桼�����ե��������
    open(DB,"$user_file");seek(DB,0,0); @userlist=<DB>;close(DB);

    if ($npc_mode){
        if (($#userlist+1 - $npc_num) >= $maxmem) {    #����Ϳ�Ķ�ᡩ
            &ERROR("��\�����������ޤ��󤬡����($maxmem��)�����С��Ǥ���") ;
        }
    }else{
        if ($#userlist+1 >= $maxmem) {    #����Ϳ�Ķ�ᡩ
            &ERROR("��\�����������ޤ��󤬡����($maxmem��)�����С��Ǥ���") ;
        }
    }

    #��ʣ�����å�
    foreach $userlist(@userlist) {
        ($w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,$w_group,$w_gpass,$w_a_name,$w_feel,$w_host,$w_os) = split(/,/, $userlist);
        if (($c_id eq $w_id) && ($c_password eq $w_password) && ($w_hit > 0)) {   #Ʊ��ID?
            $newerror = "$now,$year/$month/$mday $hour:$min:$sec,$host,cookie,$c_id $w_id,\n";
            open(DB,">>$error_file"); seek(DB,0,0); print DB $newerror; close(DB);
            &ERROR("����饯����ʣ����Ͽ�϶ػߤ��Ƥ��ޤ��������ͤˤ��䤤��碌����������") ;
        }
        if ($IP_deny && ($host eq $w_host) && (($w_hit > 0) || ($w_death eq "���ܤˤ��跺"))) {   #Ʊ��ɣ�
            $newerror = "$now,$year/$month/$mday $hour:$min:$sec,$host($os),host,$w_id,\n";
            open(DB,">>$error_file"); seek(DB,0,0); print DB $newerror; close(DB);
            &ERROR("����饯����ʣ����Ͽ�϶ػߤ��Ƥ��ޤ��������ͤˤ��䤤��碌����������") ;
        }
    }
}

#==================#
# �� ��������ɽ��  #
#==================#
sub ICON {

    local($i,$j,$stop);

    &HEADER ;
    print "<center><hr width=\"75%\">\n";
    print "<b><big>�������󥵥�ץ�</big></b>\n";
    print "<P><small>- ������Ͽ����Ƥ��륢������ϰʲ��ΤȤ���Ǥ� -</small>\n";
    print "<hr width=\"75%\">\n";
    print "<P><table border=1 cellpadding=5 cellspacing=0 width=\"600\">\n";
    print "<tr align=\"center\">\n";

    $i=0; $j=0;
    $stop = $icon_check2;
    foreach (0 .. $icon_check2-1) {
        $i++; $j++;
        print "<td><img src=\"$imgurl$icon_file[$_]\" ALIGN=middle alt=\"$icon_name[$_]\"><BR>$icon_name[$_]</td>\n";
        if ($j != $stop && $i >= 7) { print "</tr><tr align=\"center\">\n"; $i=0; }
        elsif ($j == $stop) {
            if ($i == 0) { last; }
            while ($i < 7) { print "<td><br></td>"; $i++; }
        }
    }
    print "</tr></table><br>\n";

    # ���ѥ�������
    print "<hr width=\"75%\">\n";
    print "<b><big>���ѥ�������</big></b>\n";
    print "<P><small>- ������Ͽ����Ƥ������ѥ�������ϰʲ��ΤȤ���Ǥ� -</small>\n";
    print "<hr width=\"75%\">\n";
    print "<P><table border=1 cellpadding=5 cellspacing=0 width=\"600\">\n";
    print "<tr align=\"center\">\n";

    $i=0; $j=0;
    $stop = $icon_check3 - $icon_check2;
    foreach ($icon_check2 .. $icon_check3-1) {
        $i++; $j++;
        print "<td><img src=\"$imgurl$icon_file[$_]\" ALIGN=middle alt=\"$icon_name[$_]\"><BR>$icon_name[$_]</td>\n";
        if ($j != $stop && $i >= 7) { print "</tr><tr align=\"center\">\n"; $i=0; }
        elsif ($j == $stop) {
            if ($i == 0) { last; }
            while ($i < 7) { print "<td><br></td>"; $i++; }
        }
    }
    print "</tr></table><br>\n";

    print "<FORM><INPUT TYPE=\"button\" VALUE=\"  CLOSE  \" onClick=\"top.close();\"></FORM>\n";
    &FOOTER;

}
1
