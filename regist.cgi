#! /usr/local/bin/perl
require "jcode.pl";
require "br.cgi";
require "$LIB_DIR/lib.cgi";
require "$LIB_DIR/lib2.cgi";
&LOCK;
require "pref.cgi";

&DECODE;
&CREAD ;

if ($mode eq "regist") { &REGIST; }
elsif ($mode eq "info") { &INFO; }
elsif ($mode eq "info2") { &INFO2; }
else { &MAIN; }
&UNLOCK;
exit;

#==================#
# �� �ᥤ��        #
#==================#
sub MAIN {
    &checker;

&HEADER;
print <<"_HERE_";
<P align="center"><B><FONT color=\"#ff0000\" size=\"+3\" face=\"�ͣ� ��ī\">ž����³��</FONT></B><BR><BR>
<BR>
�ط���ž�������͡��ͤ�ôǤ�Ǥ���<BR>
���̤���ϡ��֤Ȥ�ܡפȤ������Ƥ뤱�ɤ͡�<BR>
��������ʻ��Ϥɤ��Ǥ⤤���͡�<BR>
<BR>
�Ȥꤢ�����������˻�̾�ȡ����̤������ơ�<BR>
��Ф��Ƥ�館�뤫�ʡ�</P>
<CENTER>
<FORM METHOD="POST"  ACTION="regist.cgi">
<INPUT TYPE="HIDDEN" NAME="mode" VALUE="regist">
����<INPUT size="16" type="text" name="F_Name" maxlength="16"><BR>
̾��<INPUT size="16" type="text" name="L_Name" maxlength="16"><BR>
<BR>
���̡�<SELECT name="Sex">
  <OPTION value="NOSEX" selected>- ���� -</OPTION>
  <OPTION value="�˻�">�˻�</OPTION>
  <OPTION value="����">����</OPTION>
</SELECT>
_HERE_

if($icon_mode){
    print "����������<SELECT name=\"Icon\">\n";
    print "<OPTION value=\"NOICON\" selected>- �������� -</OPTION>\n";
    if($icon_check2 == 0){
        for ($i=0;$i<$#icon_file + 1;$i++){
            print "<OPTION value=\"$i\">$icon_name[$i]</OPTION>\n";
        }
    }else{
        for ($i=0;$i<$icon_check2;$i++){
            print "<OPTION value=\"$i\">$icon_name[$i]</OPTION>\n";
        }
    }

    print "</SELECT>\n";
}

print <<"_HERE_";
<BR><BR>
ID��<INPUT size="8" type="text" name="Id" maxlength="8">���ѥ���ɡ�<INPUT size="8" type="text" name="Password" maxlength="8"><BR>
��ID,�ѥ���ɤ�Ⱦ�ѱѿ���8ʸ�������<BR>
<BR>
���ʡ�<INPUT size="32" type="text" name="Message" maxlength="64"><BR>
����껦��������졣���ѣ���ʸ���ޤǡ�<BR>
�����<INPUT size="32" type="text" name="Message2" maxlength="64"><BR>
�ʼ�ʬ��˴��������<BR>
���ʥ��ԡ��롧<INPUT size="32" type="text" name="Comment" maxlength="64"><BR>
�ʰ�������ȡ���¸�԰����˵��ܤ���롣��<BR>
<BR>
<FONT color="#ffff00" size="+1"><B>Ʊ��ץ쥤�䡼��ʣ����Ͽ��������������Ѥ�<BR>
»�ʤ�̾������Ͽ�Ϥ���θ����������<BR>
���㡧����̾����̾��Ƚ�ǽ���ʤ�̾�������̤Ȱ㤦̾���������̾����<BR>
�����ͤΰ�¸�ǥǡ�������������ޤ���<BR>
</B></FONT><BR>
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
    &checker;

    #���Ͼ�������å�
    if ($f_name2 eq '') { &ERROR("����̤���ϤǤ���") ; }
    elsif (length($f_name2) > 8) { &ERROR("����ʸ�����������С����Ƥ��ޤ��������ѣ�ʸ���ޤǡ�") ; }
    elsif ((grep /[a-z]|[A-Z]|[0-9]/, $f_name2) == 1) { &ERROR("��̾��Ⱦ��ʸ�������ѤǤ��ޤ��󡣡����ѣ�ʸ���ޤǡ�") ; }
    elsif ($l_name2 eq '') { &ERROR("̾��̤���ϤǤ���") ; }
    elsif (length($l_name2) > 8) { &ERROR("̾��ʸ�����������С����Ƥ��ޤ��������ѣ�ʸ���ޤǡ�") ; }
    elsif ((grep /[a-z]|[A-Z]|[0-9]/, $l_name2) == 1) { &ERROR("��̾��Ⱦ��ʸ�������ѤǤ��ޤ��󡣡����ѣ�ʸ���ޤǡ�") ; }
    elsif ($sex2 eq "NOSEX") { &ERROR("���̤�̤����Ǥ���") ; }
    elsif (length($id2) > 8) { &ERROR("ID��ʸ�����������С����Ƥ��ޤ�����Ⱦ��8ʸ���ޤǡ�") ; }
    elsif ($id2 eq '') { &ERROR("ID��̤���ϤǤ���") ; }
    elsif ((grep /[a-z]|[A-Z]|[0-9]/, $id2) == 0) { &ERROR("ID��Ⱦ�Ѥ����Ϥ��Ƥ�����������Ⱦ�ѣ�ʸ���ޤǡ�") ; }
    elsif ($id2 =~ /\_|\,|\;|\<|\>|\(|\)|&|\/|\./) { &ERROR("�ɣĤ˻��Ѷػ�ʸ�������äƤ��ޤ���") ; }
    elsif ($password2 eq '') { &ERROR("�ѥ���ɤ�̤���ϤǤ���") ; }
    elsif (length($password2) > 8) { &ERROR("�ѥ���ɤ�ʸ�����������С����Ƥ��ޤ�����Ⱦ�ѣ�ʸ���ޤǡ�") ; }
    elsif ((grep /[a-z]|[A-Z]|[0-9]/, $password2) == 0) { &ERROR("password��Ⱦ�Ѥ����Ϥ��Ƥ�����������Ⱦ�ѣ�ʸ���ޤǡ�") ; }
    elsif ($password2 =~ /\_|\,|\;|\<|\>|\(|\)|&|\/|\./) { &ERROR("�ѥ���ɤ˻��Ѷػ�ʸ�������äƤ��ޤ���") ; }
    elsif ($icon2 eq "NOICON") { &ERROR("��������̤����Ǥ���") ; }
    elsif ($id2 eq $password2) { &ERROR("ID��Ʊ��ʸ����ϥѥ���ɤ˻Ȥ��ޤ���") ; } #joe�����å�(^_^;)
    elsif (length($msg2) > 64) { &ERROR("���ʤ�ʸ�����������С����Ƥ��ޤ��������ѣ���ʸ���ޤǡ�") ; }
    elsif (length($dmes2) > 64) { &ERROR("�����ʸ�����������С����Ƥ��ޤ��������ѣ���ʸ���ޤǡ�") ; }
    elsif (length($com2) > 64) { &ERROR("�����Ȥ�ʸ�����������С����Ƥ��ޤ��������ѣ���ʸ���ޤǡ�") ; }
    elsif ($icon_check && $icon_mode){
        if(($sex2 =~ /�˻�/)&&($icon2 >= $icon_check )) { &ERROR("���̤Ȱ㤦������������򤷤Ƥ��ޤ���") ; }
        elsif(($sex2 =~ /����/)&&($icon2 < $icon_check )){ &ERROR("���̤Ȱ㤦������������򤷤Ƥ��ޤ���") ; }
    }

    #�桼���ե��������
    open(DB,"$user_file");seek(DB,0,0); @userlist=<DB>;close(DB);

    #Ʊ��Ʊ̾���ɣĥ����å�
    foreach $userlist(@userlist) {
        ($w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf) = split(/,/, $userlist);
        if (($id2 eq $w_id) || (($f_name2 eq $w_f_name)&&($l_name2 eq $w_l_name)&&($w_sts ne "��˴"))) {    #Ʊ��ID or Ʊ��Ʊ̾?
            &ERROR("Ʊ��ɣġ��㤷���ϡ�Ʊ��Ʊ̾�Υ���饯��������¸�ߤ��ޤ���") ;
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
    $hit = int(rand(20)) + 30 ;
    $mhit = $hit ;
    $kill=0;
    $sta = $maxsta ;
    $level=1; $exp=0;
    $death = $msg = "";
    $sts = "����"; $pls=0;
    $tactics = "�̾�" ;
    $endtime = 0 ;
    $log = "";
    $dmes = "" ; $bid = "" ; $inf = "" ;

    #��������ƥ������������
    $item[0] = "�ѥ�<>SH"; $eff[0] = 20; $itai[0] = 2;
    $item[1] = "��<>HH"; $eff[1] = 15; $itai[1] = 2;
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
        $item[3] = "�ƴ�<>Y"; $eff[3] = 12; $itai[3] = 1;
        $item[4] = $st_item; $eff[4] = $st_eff; $itai[4] = $st_tai;
    } elsif ($w_wep =~ /<>WA/) {    #��
        $item[3] = "��<>Y"; $eff[3] = 12; $itai[3] = 1;
        $item[4] = $st_item; $eff[4] = $st_eff; $itai[4] = $st_tai;
    } else {
        $item[3] = $st_item; $eff[3] = $st_eff; $itai[3] = $st_tai;
    }

    &CLUBMAKE ; #����ֺ���

    #�桼���ե�����
    open(DB,"$user_file");seek(DB,0,0); @userlist=<DB>;close(DB);

    $newuser = "$id2,$password2,$f_name2,$l_name2,$sex2,$cl,$no,$endtime,$att,$def,$hit,$mhit,$level,$exp,$sta,$wep,$watt,$wtai,$bou,$bdef,$btai,$bou_h,$bdef_h,$btai_h,$bou_f,$bdef_f,$btai_f,$bou_a,$bdef_a,$btai_a,$tactics,$death,$msg2,$sts,$pls,$kill,$icon2,$item[0],$eff[0],$itai[0],$item[1],$eff[1],$itai[1],$item[2],$eff[2],$itai[2],$item[3],$eff[3],$itai[3],$item[4],$eff[4],$itai[4],$item[5],$eff[5],$itai[5],$log,$dmes2,$bid,$club,$wn,$wp,$wa,$wg,$we,$wc,$wd,$wb,$wf,$ws,$com2,$inf,\n" ;

    #�����桼�������Ǽ
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
<A href="regist.cgi?mode=info&Id=$id2&Password=$password2"><B><FONT color="#ff0000" size="+2">����ι�Ԥؽ�ȯ</FONT></B></A><BR>
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
<P align="center"><B><FONT color=\"#ff0000\" size=\"+3\" face=\"�ͣ� ��ī\">��Ͽ��λ</FONT></B><BR><BR>
�ܤ������ȡ������Τ褦�ʽ�ˤ���������ι�Ԥ˹Ԥä��Ϥ��ʤΤˡ�������<BR>
�֤�����������ι�Ԥ˹Ԥ��Х�����ǵޤ�̲�������äƤ��ơ�������<BR>
������Ϥ��ȡ�¾�����̤⤤��褦�����褯����ȡ������俧�μ��ؤ��Ϥ���Ƥ�����˵��Ť���<BR>
��ʬ�μ�˿����ȡ��䤿����°�δ���������äƤ�����<BR>
����Ʊ�͡����ζ俧�μ��ؤ��Ϥ���Ƥ�����<BR>
<BR>
�����������⤫�顢��ͤ��ˤ����äƤ�����������<BR><BR>
<BR>
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

    $wa=$wg=$wb=$wc=$wd=$ws=$wn=$wf=$wp=$we=0 ;

    local($dice) = int(rand(11)) ;

    if ($dice == 0) {
        $club = "��ƻ��" ;
        $wa = 1 * $BASE ;
    }elsif ($dice == 1) {
        $club = "�ͷ���" ;
        $wg = 1 * $BASE ;
    }elsif ($dice == 2) {
        $club = "������" ;
        $wb = 1 * $BASE ;
    }elsif ($dice == 3) {
        $club = "�Х�����" ;
        $wc = 1 * $BASE ;
    }elsif ($dice == 4) {
        $club = "�ʳ���" ;
        $wd = 1 * $BASE ;
    }elsif ($dice == 5) {
        $club = "�ե��󥷥���" ;
        $ws = 1 * $BASE ;
    }elsif ($dice == 6) {
        $club = "��ƻ��" ;
        $wn = 1 * $BASE ;
    }elsif ($dice == 7) {
        $club = "�ܥ�������" ;
        $wp = 1 * $BASE ;
    }elsif ($dice == 8) {
        $club = "Φ����" ;
    }elsif ($dice == 9) {
        $club = "����������" ;
    }elsif ($dice == 10) {
        $club = "�ѥ�������" ;
    }

}

#==================#
# �� �����å�      #
#==================#
sub checker{
    if(($limit == "")||($limit == 0)){ $limit = 7; }
    local($t_limit) = ($limit * 3) + 1;

    if (($fl =~ /��λ/)||($ar >= $t_limit)){
        &ERROR("�ץ����μ��դϽ�λ�������ޤ�����<br><br>������ץ���೫�Ϥ��Ԥ���������") ;
    }


    $chktim = $c_endtime + (1*60*60*2) ;    #��˴���ּ���
    ($sec,$min,$hour,$mday,$month,$year,$wday,$yday,$isdst) = localtime($chktim);
    $year+=1900; $month++;

    if ($chktim > $now) {   #��Ͽ���֥��顼��
        &ERROR("������˴��ǧ�塢�����֤Ϻ���Ͽ����ޤ���<br><br>��������Ͽ��ǽ\���֡�$year/$month/$mday $hour:$min:$sec") ;
    }

    $IP_chk = 1;
    foreach $ipok(@IP_ok){
        if($IP_host){
            if($host =~ /$ipok$/){ $IP_chk = 0; last;}
        }else{
            if($host =~ /^$ipok/){ $IP_chk = 0; last;}
        }
    }

    if(($IP_deny)&&($IP_chk)){
        #���ե��������
        open(DB,"$log_file");seek(DB,0,0); @loglist=<DB>;close(DB);

        foreach $loglist(reverse(@loglist)) {
            ($gettime,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_f_name2,$w_l_name2,$w_sex2,$w_cl2,$w_no2,$getkind,$log_host)= split(/,/, $loglist);
            if($loglist =~ /ENTRY/){
                $hostdat{"$w_f_name$w_l_name"} = "$log_host";
            }elsif($loglist =~ /DEATH/){
                $chktim = $gettime + (1*60*60*2) ;    #��˴���ּ���
                if ($chktim < $now) {
                    delete $hostdat{"$w_f_name$w_l_name"};
                }
            }
        }

        foreach $log_host(values(%hostdat)) {
            $hostlist = ( $hostlist . "$log_host ");
        }

        if($hostlist =~ /$host/){&ERROR("����饯����ʣ����Ͽ�϶ػߤ��Ƥ��ޤ��������ͤˤ��䤤��碌����������") ;}

    }

    #�桼�����ե��������
    open(DB,"$user_file");seek(DB,0,0); @userlist=<DB>;close(DB);
    $listnum = @userlist;
    if ($npc_mode){
        if (($listnum - $npc_num) >= $maxmem) {    #����Ϳ�Ķ�ᡩ
            &ERROR("��\�����������ޤ��󤬡����($maxmem��)�����С��Ǥ���") ;
        }
    }else{
        if ($listnum >= $maxmem) {    #����Ϳ�Ķ�ᡩ
            &ERROR("��\�����������ޤ��󤬡����($maxmem��)�����С��Ǥ���") ;
        }
    }

    #��ʣ�����å�
    foreach $userlist(@userlist) {
        ($w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf) = split(/,/, $userlist);
        if (($c_id eq $w_id) && ($c_password eq $w_password) && ($w_sts ne "��˴")) {   #Ʊ��ID or Ʊ��Ʊ̾?
            &ERROR("����饯����ʣ����Ͽ�϶ػߤ��Ƥ��ޤ��������ͤˤ��䤤��碌����������") ;
        }
    }
}

