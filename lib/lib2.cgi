# ���ѥ��֥롼����

#==================#
# �� ID�����å�����#
#==================#
sub IDCHK {


    open(DB,"$user_file");seek(DB,0,0); @userlist=<DB>;close(DB);


    $mem=0;
    $chksts = "NG";
    for ($i=0; $i<$#userlist+1; $i++) {
        ($w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf) = split(/,/, $userlist[$i]);
        if ($w_id eq $id2) {    #ID���ס�
            if ($w_password eq $password2) {    #�ѥ�������
                if ($w_hit > 0) {
                    $chksts = "OK";$Index=$i;$mem++;$plsmem[$w_pls]++ ;
                    ($id,$password,$f_name,$l_name,$sex,$cl,$no,$endtime,$att,$def,$hit,$mhit,$level,$exp,$sta,$wep,$watt,$wtai,$bou,$bdef,$btai,$bou_h,$bdef_h,$btai_h,$bou_f,$bdef_f,$btai_f,$bou_a,$bdef_a,$btai_a,$tactics,$death,$msg,$sts,$pls,$kill,$icon,$item[0],$eff[0],$itai[0],$item[1],$eff[1],$itai[1],$item[2],$eff[2],$itai[2],$item[3],$eff[3],$itai[3],$item[4],$eff[4],$itai[4],$item[5],$eff[5],$itai[5],$log,$dmes,$bid,$club,$wn,$wp,$wa,$wg,$we,$wc,$wd,$wb,$wf,$ws,$com,$inf) = split(/,/, $userlist[$i]);
                    &CSAVE;
                    #�������ɹ�

                    open(DB,"$gun_log_file");seek(DB,0,0); @gunlog=<DB>;close(DB);

                    local($guntime,$gunpls,$wid,$wid2,$a) = split(/,/,$gunlog[0]) ;
                    if (($now < ($guntime+(15)))&& ($wid ne $id) && ($wid2 ne $id)) {   #�ƻ��Ѥ���15�ð��⡩
                        $jyulog = "<font color=\"yellow\"><b>$gunpls �����ǡ�������ʹ��������������</b></font><br>" ;
                    } else { $jyulog = "" ; }
                    local($guntime,$gunpls,$wid,$wid2,$a) = split(/,/,$gunlog[1]) ;
                    if (($now < ($guntime+(15)))&& ($wid ne $id) && ($wid2 ne $id) && ($place[$pls] eq $gunpls)) {  #��������15�ð��⡩
                        $jyulog2 = "<font color=\"yellow\"><b>�᤯�����Ĥ���ï���������줿�Τ���������</b></font><br>" ;
                    } else { $jyulog2 = "" ; }
                    local($guntime,$gunpls,$wid,$wid2,$a) = split(/,/,$gunlog[2]) ;
                    if (($now < ($guntime+(30)))) { #���ԡ������Ѥ���30�ð��⡩
                        $jyulog3 = "<font color=\"yellow\"><b>$gunpls ��������$wid������ʹ�����롦����</b></font><br><font color=\"lime\"><b>��$wid2��</b></font><br>" ;
                    } else { $jyulog3 = "" ; }
                } else {
                    &CDELETE;
                    &ERROR("���˻�˴���Ƥ��ޤ���<BR><BR>�����$w_death<BR><BR><font color=\"lime\"><b>$w_msg</b></font><br>") ;
                }
            } else {
                &ERROR("�ѥ���ɤ����פ��ޤ���") ;
            }
        } else {
            if ($w_hit > 0) {
                $plsmem[$w_pls]++ ;
                if ($w_sts ne "NPC0"){ $mem ++ ; }
                }
        }
    }

    if ($chksts eq "NG") {
        &ERROR("�ɣĤ����Ĥ���ޤ���") ;
    }

    local($b_limit) = ($battle_limit * 3) + 1;
    if ((($mem == 1) && ($inf =~ /��/) && ($ar > $b_limit))||(($mem == 1) && ($ar > $b_limit))) {    #ͥ����
        if($fl !~ /��λ/){
            open(FLAG,">$end_flag_file"); print(FLAG "��λ\n"); close(FLAG);
            &LOGSAVE("WINEND1");
        }
        require "$LIB_DIR/ending.cgi";
        &ENDING;
    }elsif ($inf =~ /��/){
        require "$LIB_DIR/ending.cgi";
        &ENDING;
    }elsif ($fl =~ /���/){
        require "$LIB_DIR/ending.cgi";
        &ENDING;
    } else {
        if ($log ne '') {$wlog = $log ;$log="";&SAVE;$log=$wlog;}
        $bid = "" ;
    }
}

#==================#
# �� ���ơ�������  #
#==================#
sub STS {

    local($watt_2) = 0 ;

    if (($Command ne "INN2")&&($Command ne "HEAL2")) {
        $up = int(($now - $endtime) / (1*$kaifuku_time));
        if ($inf =~ /ʢ/) { $up = int($up / 2) ; }
        if ($sts eq "��̲") {
            $maxp = $maxsta - $sta ;    #�����ͤޤǤ�����
            if ($up > $maxp) { $up = $maxp ; }
            $sta += $up ;
            if ($sta > $maxsta) { $sta = $maxsta ; }
            $log = ($log . "��̲�η�̡������ߥʤ� $up ����������<BR>") ;
            $sts = "����"; $endtime = 0 ;
            &SAVE ;
        } elsif ($sts eq "����") {
            if ($kaifuku_rate == 0){$kaifuku_rate = 1;}
            $up = int($up / $kaifuku_rate) ;
            $maxp = $mhit - $hit ;  #�����ͤޤǤ�����
            if ($up > $maxp) { $up = $maxp ; }
            $hit += $up ;
            if ($hit > $mhit) { $hit = $mhit ; }
            $log = ($log . "���Ťη�̡����Ϥ� $up ����������<BR>") ;
            $sts = "����"; $endtime = 0 ;
            &SAVE ;
        }
    }

    ($w_name,$w_kind) = split(/<>/, $wep);
    ($b_name,$b_kind) = split(/<>/, $bou);

    $up = int(($level*$baseexp)+(($level-1)*$baseexp)) ;

    $cln = "$cl $sex$no��" ;

    if (($w_kind =~ /G|A/) && ($wtai == 0)) { #���� or ��̵���� or ��̵����
        $watt_2 = int($watt/10) ;
    } else {
        $watt_2 = $watt ;
    }

    $ball = $bdef + $bdef_h + $bdef_a + $bdef_f ;
    if ($item[5] =~ /AD/) {$ball += $eff[5];} #�������ɶ�

    if($icon_mode){ $colum = 2;}else{$colum = 3;}

print <<"_HERE_";
<P align="center"><B><FONT color="#ff0000" size="+3" face="�ͣ� ��ī">$place[$pls]��$area[$pls]��</FONT></B><BR>
</P>
<TABLE width="568">
<TR><TD><B><FONT color="#ff0000">
@links
</FONT></B></TD></TR>
</TABLE>

<TABLE width="568">
  <TBODY>
    <TR>
      <TD valign="top" width="279" height="311">
      <TABLE border="1" width="389" cellspacing="0" height="300">
        <TBODY>
          <TR>
            <TD colspan="4" align="center"><B>���ơ�����</B></TD>
          </TR>
          <TR>
_HERE_
            if($icon_mode){
                print "<TD ROWSPAN=\"3\" width=\"70\"><IMG src=\"$imgurl$icon_file[$icon]\" width=\"70\" height=\"70\" border=\"0\" align=\"middle\"></TD>\n";
            }
print <<"_HERE_";
            <TD width="60"><B>���ᡡ̾</B></TD>
            <TD colspan="$colum" width="224">$f_name $l_name</TD>
          </TR>
          <TR>
            <TD><B>�����ֹ�</B></TD>
            <TD colspan="$colum">$cln</TD>
          </TR>
          <TR>
            <TD ><B>����Ľ�</B></TD>
_HERE_
            $kega ="" ;
            if ($inf =~ /Ƭ/) {$kega = ($kega . "Ƭ����") ;}
            if ($inf =~ /��/) {$kega = ($kega . "�ӡ�") ;}
            if ($inf =~ /ʢ/) {$kega = ($kega . "ʢ����") ;}
            if ($inf =~ /­/) {$kega = ($kega . "­��") ;}
            if ($kega eq "") { $kega = "��" ;}
print <<"_HERE_";
            <TD colspan="$colum">$kega</TD>
          </TR>
          <TR>
            <TD width="45"><B>��٥�</B></TD>
            <TD width="45">$level</TD>
            <TD width="45"><B>�и���</B></TD>
            <TD>$exp/$up</TD>
          </TR>
          <TR>
            <TD><B>����</B></TD>
            <TD>$hit/$mhit</TD>
            <TD><B>�����ߥ�</B></TD>
            <TD>$sta/$maxsta</TD>
          </TR>
          <TR>
            <TD><B>������</B></TD>
            <TD>$att+$watt_2</TD>
            <TD><B>���</B></TD>
            <TD>$w_name/$wtai</TD>
          </TR>
          <TR>
            <TD><B>�ɸ���</B></TD>
            <TD>$def+$ball</TD>
            <TD><B>�ɶ�</B></TD>
            <TD>$b_name/$btai</TD>
          </TR>
          <TR>
            <TD height="9" colspan="4" align="center"><B>�����</B></TD>
          </TR>
          <TR>
            <TD colspan="4" height="80" valign="top">
_HERE_

            for ($i=0; $i<5; $i++) {
                if ($item[$i] ne "�ʤ�") {
                    ($i_name,$i_kind) = split(/<>/, $item[$i]);
                    print "$i_name/$eff[$i]/$itai[$i]<BR>\n";
                }
            }

print <<"_HERE_";
            </TD>
          </TR>
        </TBODY>
      </TABLE>
      </TD>
      <TD valign="top" width="200" height="310">
      <TABLE border="1" cellspacing="0">
        <TBODY>
          <TR><TD align="center" width="250"><B>���ޥ��</B></TD>
          <TR>
            <TD align="left" valign="top" height="280" width="240">
            <FORM METHOD="POST">
            <INPUT TYPE="HIDDEN" NAME="mode" VALUE="command">
            <INPUT TYPE="HIDDEN" NAME="Id" VALUE="$id2">
            <INPUT TYPE="HIDDEN" NAME="Password" VALUE="$password2">
_HERE_

            &COMMAND;

print <<"_HERE_";
            </FORM>
            </TD>
          </TR>
        </TBODY>
      </TABLE>
      </TD>
    </TR>
    <TR>
      <TD colspan="2" valign="top" height="101">
      <TABLE border="1" cellspacing="0" height="150" cellpadding="0">
        <TBODY>
          <TR>
            <TD height="20" valign="top" width="600">$log</TD>
          </TR>
        </TBODY>
      </TABLE>
      </TD>
    </TR>
  </TBODY>
</TABLE>
<BR>
_HERE_
}

#==================#
# �� �ǥ����ɽ���  #
#==================#
sub DECODE {
    $p_flag=0;
        if ($ENV{'REQUEST_METHOD'} eq "POST") {
            $p_flag=1;
            if ($ENV{'CONTENT_LENGTH'} > 51200) {
                &ERROR("�۾�����ϤǤ�"); }
            read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
        } else { $buffer = $ENV{'QUERY_STRING'}; }
    @pairs = split(/&/, $buffer);
    foreach (@pairs) {
        ($name,$value) = split(/=/, $_);
        $value =~ tr/+/ /;
        $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

        &jcode::convert(*value, "euc", "", "z");
        &jcode::tr(\$value, '��', ' ');

        $value =~ s/&amp;/&/g;
        $value =~ s/&lt;/</g;
        $value =~ s/&gt;/>/g;
        $value =~ s/&quot;/"/g;
        $value =~ s/&nbsp;/ /g;

        $value =~ s/&/&amp;/g;
        $value =~ s/</&lt;/g;
        $value =~ s/>/&gt;/g;
        $value =~ s/"/&quot;/g;
        $value =~ s/ /&nbsp;/g;
        $value =~ s/,/��/g; #�ǡ�����»�к�

        $in{$name} = $value;
    }

    $mode = $in{'mode'};
    $id2 = $in{'Id'};
    $password2 = $in{'Password'};

    $Command = $in{'Command'};
    $Command2 = $in{'Command2'};

    $l_name2 = $in{'L_Name'} ;
    $f_name2 = $in{'F_Name'} ;
    $msg2 = $in{'Message'} ;
    $dmes2 = $in{'Message2'} ;
    $dengon = $in{'Dengon'} ;
    $com2 = $in{'Comment'} ;
    $sex2 = $in{'Sex'};
    $icon2 = $in{'Icon'};
    $itno2 = $in{'Itno'};
    $getid = $in{'WId'};
    $speech = $in{'speech'};

    srand;

}

#==================#
# �� ��˥塼��    #
#==================#
sub COMMAND {

    local($i) = 0 ;

    if (($Command eq "INN2") || ($Command eq "HEAL2") || ($Command eq "KEIKAI2")) {
        if ($Command eq "HEAL2") {
            $log = ($log . "����μ��Ť򤷤褦��<BR>") ;
            $sts = "����" ;
            print "�����桦������<BR><BR>\n";
            print "��<INPUT type=\"radio\" name=\"Command\" value=\"HEAL2\" checked>����<BR><BR>\n";
        } else {
            $log = ($log . "�������Ƥ�������<BR>") ;
            $sts = "��̲" ;
            print "��̲�桦������<BR><BR>\n";
            print "��<INPUT type=\"radio\" name=\"Command\" value=\"INN2\" checked>��̲<BR><BR>\n";
        }
        print "��<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\">���<BR><BR>\n";
        print "��<INPUT type=\"submit\" name=\"Enter\" value=\"����\">\n";
        return ;
    }

    if (($Command eq '')||($Command eq "MAIN")) {   #MAIN
        $log = ($log . "$jyulog$jyulog2$jyulog3���ơ��ɤ����褦��������<br>") ;
        print "����Ԥ��ޤ�����<BR><BR>\n";
        if ($place[$pls] eq "ʬ��") {
            print "��<INPUT type=\"radio\" name=\"Command\" value=\"MOVE\" checked>��ư<BR>\n";
            if ($hackflg == 1) {
                print "��<INPUT type=\"radio\" name=\"Command\" value=\"SEARCH\">õ��<BR>\n";
            }
            print "��<INPUT type=\"radio\" name=\"Command\" value=\"ITMAIN\">�����ƥ�<BR>\n";
            print "��<INPUT type=\"radio\" name=\"Command\" value=\"SPECIAL\">�ü�\<BR>\n";
            print "��<INPUT type=\"radio\" name=\"Command\" value=\"USRSAVE\">������\<BR>\n";
        } else {
            print "��<INPUT type=\"radio\" name=\"Command\" value=\"MOVE\" checked>��ư<BR>\n";
            print "��<INPUT type=\"radio\" name=\"Command\" value=\"SEARCH\">õ��<BR>\n";
            print "��<INPUT type=\"radio\" name=\"Command\" value=\"ITMAIN\">�����ƥ�<BR>\n";
            print "��<INPUT type=\"radio\" name=\"Command\" value=\"HEAL\">����<BR>\n";
            print "��<INPUT type=\"radio\" name=\"Command\" value=\"INN\">��̲<BR>\n";
            print "��<INPUT type=\"radio\" name=\"Command\" value=\"SPECIAL\">�ü�\<BR>\n";
            print "��<INPUT type=\"radio\" name=\"Command\" value=\"USRSAVE\">������\<BR>\n";
        }
        print "<BR>\n";
        print "��<INPUT type=\"submit\" name=\"Enter\" value=\"����\">\n";
    } elsif ($Command eq "MOVE") {  #��ư

        $log = ($log . "$place[$pls]���顢¾�ξ��ذ�ư���뤫��������<br>") ;
        print "����عԤ��ޤ�����<BR><BR>\n";
        print "��<select name=\"Command\">\n" ;
        print "<option value=\"MAIN\" selected>���\n";
        for ($j=0; $j<$#place+1; $j++) {
            if ($place[$j] ne $place[$pls]) {
                print "<option value=\"MV$j\">$place[$j]($area[$j])</option>\n";
            }
        }
        print "</select><BR><BR>\n";
        print "��<INPUT type=\"submit\" name=\"Enter\" value=\"����\">\n";
    } elsif ($Command eq "ITEM") {  #�����ƥ�
        $log = ($log . "�ǥ��ѥå�����ˤϡ��������äƤ������ʡ�������<BR>") ;
        print "������Ѥ��ޤ�����<BR><BR>\n";
        print "��<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>���<BR><BR>\n";
        for ($i=0; $i<5; $i++) {
            if ($item[$i] ne "�ʤ�") {
                ($in, $ik) = split(/<>/, $item[$i]);
                print "��<INPUT type=\"radio\" name=\"Command\" value=\"ITEM_$i\">$in/$eff[$i]/$itai[$i]<BR>\n";
            }
        }
        print "<BR>\n";
        print "��<INPUT type=\"submit\" name=\"Enter\" value=\"����\">\n";
    } elsif ($Command eq "DEL") {   #�����ƥ����
        $log = ($log . "�ǥ��ѥå�������������뤫��������<BR>") ;
        print "����ΤƤޤ�����<BR><BR>\n";
        print "��<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>���<BR><BR>\n";
        for ($i=0; $i<5; $i++) {
            if ($item[$i] ne "�ʤ�") {
                ($in, $ik) = split(/<>/, $item[$i]);
                print "��<INPUT type=\"radio\" name=\"Command\" value=\"DEL_$i\">$in/$eff[$i]/$itai[$i]<BR>\n";
            }
        }
        print "<BR>\n";
        print "��<INPUT type=\"submit\" name=\"Enter\" value=\"����\">\n";
    } elsif ($Command eq "SEIRI") { #�����ƥ�����
        $log = ($log . "�ǥ��ѥå�������������뤫��������<BR>") ;
        print "���Ȳ���Ż��ޤ�����<BR><BR>\n";
        print "��<select name=\"Command\">\n" ;
        print "��<option value=\"MAIN\" selected>�ߤ��</option>\n";
        for ($i=0; $i<5; $i++) {
            if ($item[$i] ne "�ʤ�") {
                ($in, $ik) = split(/<>/, $item[$i]);
                print "��<option value=\"SEIRI_$i\">$in/$eff[$i]/$itai[$i]</option>\n";
            }
        }
        print "</select><BR>\n" ;
        print "<BR>\n";
        print "��<select name=\"Command2\">\n" ;
        print "��<option value=\"MAIN\" selected>�ߤ��</option>\n";
        for ($i2=0; $i2<5; $i2++) {
            if ($item[$i2] ne "�ʤ�") {
                ($in2, $ik2) = split(/<>/, $item[$i2]);
                print "��<option value=\"SEIRI2_$i2\">$in2/$eff[$i2]/$itai[$i2]</option>\n";
            }
        }
        print "</select><BR>\n" ;
        print "<BR>\n";
        print "��<INPUT type=\"submit\" name=\"Enter\" value=\"����\">\n";
    } elsif ($Command eq "GOUSEI") { #�����ƥ����
        $log = ($log . "�����äƤ����Τ��Ȥ߹�碌�ơ��������ʤ����ʡ�<BR>") ;
        print "���Ȳ���������ޤ�����<BR><BR>\n";
        print "��<select name=\"Command\">\n" ;
        print "��<option value=\"MAIN\" selected>�ߤ��</option>\n";
        for ($i=0; $i<5; $i++) {
            if ($item[$i] ne "�ʤ�") {
                ($in, $ik) = split(/<>/, $item[$i]);
                print "��<option value=\"GOUSEI_$i\">$in/$eff[$i]/$itai[$i]</option>\n";
            }
        }
        print "</select><BR>\n" ;
        print "<BR>\n";
        print "��<select name=\"Command2\">\n" ;
        print "��<option value=\"MAIN\" selected>�ߤ��</option>\n";
        for ($i2=0; $i2<5; $i2++) {
            if ($item[$i2] ne "�ʤ�") {
                ($in2, $ik2) = split(/<>/, $item[$i2]);
                print "��<option value=\"GOUSEI2_$i2\">$in2/$eff[$i2]/$itai[$i2]</option>\n";
            }
        }
        print "</select><BR>\n" ;
        print "<BR>\n";
        print "��<INPUT type=\"submit\" name=\"Enter\" value=\"����\">\n";
    } elsif ($Command eq "OUKYU") { #���޽���
        $log = ($log . "����μ��Ť򤹤뤫��������<BR>") ;

        print "������Ť��ޤ�����<BR><BR>\n";
        print "��<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>���<BR><BR>\n";

        if ($inf =~ /Ƭ/) { print "��<INPUT type=\"radio\" name=\"Command\" value=\"OUK_0\">Ƭ<BR>\n"; }
        if ($inf =~ /��/) { print "��<INPUT type=\"radio\" name=\"Command\" value=\"OUK_1\">��<BR>\n"; }
        if ($inf =~ /ʢ/) { print "��<INPUT type=\"radio\" name=\"Command\" value=\"OUK_2\">ʢ��<BR>\n"; }
        if ($inf =~ /­/) { print "��<INPUT type=\"radio\" name=\"Command\" value=\"OUK_3\">­<BR>\n"; }

        print "<BR>\n";
        print "��<INPUT type=\"submit\" name=\"Enter\" value=\"����\">\n";
    } elsif ($Command =~ /BATTLE0/) {   #��Ʈ���ޥ��
        local($a,$wid) = split(/_/, $Command);
        $log = ($log . "���ơ��ɤ����褦��������") ;
        print "���򤷤ޤ�����<BR>\n";
        print "<BR>����å�����<BR>\n";
        print "��<INPUT size=\"30\" type=\"text\" name=\"Dengon\" maxlength=\"64\"><BR><BR>\n";
        $chk = "checked" ;
        ($w_name,$w_kind) = split(/<>/, $wep);
        if ($w_kind =~ /B/) {print "��<INPUT type=\"radio\" name=\"Command\" value=\"ATK_WB_$wid\" $chk>����($wb)<BR>\n"; $chk="" ;}
        if ($w_kind =~ /P/) {print "��<INPUT type=\"radio\" name=\"Command\" value=\"ATK_WP_$wid\" $chk>����($wp)<BR>\n"; $chk="" ;}
        if (($w_kind =~ /G/) && ($wtai > 0)) {print "��<INPUT type=\"radio\" name=\"Command\" value=\"ATK_WG_$wid\" $chk>���($wg)<BR>\n"; $chk="" ;}
        if (($w_kind =~ /A/) && ($wtai > 0)) {print "��<INPUT type=\"radio\" name=\"Command\" value=\"ATK_WA_$wid\" $chk>�ͤ�($wa)<BR>\n"; $chk="" ;}
        if ($w_kind =~ /N/) {print "��<INPUT type=\"radio\" name=\"Command\" value=\"ATK_WN_$wid\" $chk>�¤�($wn)<BR>\n"; $chk="" ;}
        if ($w_kind =~ /S/) {print "��<INPUT type=\"radio\" name=\"Command\" value=\"ATK_WS_$wid\" $chk>�ɤ�($ws)<BR>\n"; $chk="" ;}
        if ($w_kind =~ /C/) {print "��<INPUT type=\"radio\" name=\"Command\" value=\"ATK_WC_$wid\" $chk>�ꤲ��($wc)<BR>\n"; $chk="" ;}
        if ($w_kind =~ /D/) {print "��<INPUT type=\"radio\" name=\"Command\" value=\"ATK_WD_$wid\" $chk>�ꤲ��($wd)<BR>\n"; $chk="" ;}
        if (($w_kind !~ /S|N|C|P|D|B/)&&(($w_kind =~ /G|A/) && ($wtai == 0))) {print "��<INPUT type=\"radio\" name=\"Command\" value=\"ATK_WB_$wid\" $chk>����($wb)<BR>\n"; $chk="" ;}
        print "��<INPUT type=\"radio\" name=\"Command\" value=\"RUNAWAY\">ƨ˴<BR>\n";
        print "<BR>\n";
        print "��<INPUT type=\"submit\" name=\"Enter\" value=\"����\">\n";
    } elsif ($Command eq "BATTLE2") {   #�����ƥදå
        local($itno) = -1;
        for ($i=0; $i<5; $i++) {
            if ($item[$i] eq "�ʤ�") {
                $itno = $i ;
            }
        }
        print "����å���ޤ�����<BR><BR>\n";
        print "��<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>���<BR><BR>\n";
        print "<INPUT TYPE=\"HIDDEN\" NAME=\"Itno\" VALUE=\"$itno\">\n";
        print "<INPUT TYPE=\"HIDDEN\" NAME=\"WId\" VALUE=\"$w_id\">\n";

        if ($w_wep !~ /�Ǽ�/) { #�������
            local($in, $ik) = split(/<>/, $w_wep);
            print "��<INPUT type=\"radio\" name=\"Command\" value=\"GET_6\">$in/$w_watt/$w_wtai<BR>\n";
        }
        if ($w_bou !~ /����/) { #�ɶ�����
            local($in, $ik) = split(/<>/, $w_bou);
            print "��<INPUT type=\"radio\" name=\"Command\" value=\"GET_7\">$in/$w_bdef/$w_btai<BR>\n";
        }
        if ($w_bou_h !~ /�ʤ�/) { #�ɶ�����
            local($in, $ik) = split(/<>/, $w_bou_h);
            print "��<INPUT type=\"radio\" name=\"Command\" value=\"GET_8\">$in/$w_bdef_h/$w_btai_h<BR>\n";
        }
        if ($w_bou_f !~ /�ʤ�/) { #�ɶ�����
            local($in, $ik) = split(/<>/, $w_bou_f);
            print "��<INPUT type=\"radio\" name=\"Command\" value=\"GET_9\">$in/$w_bdef_f/$w_btai_f<BR>\n";
        }
        if ($w_bou_a !~ /�ʤ�/) { #�ɶ�����
            local($in, $ik) = split(/<>/, $w_bou_a);
            print "��<INPUT type=\"radio\" name=\"Command\" value=\"GET_10\">$in/$w_bdef_a/$w_btai_a<BR>\n";
        }

        for ($i=0; $i<6; $i++) {
            if ($w_item[$i] ne "�ʤ�") {
                local($in, $ik) = split(/<>/, $w_item[$i]);
                print "��<INPUT type=\"radio\" name=\"Command\" value=\"GET_$i]\">$in/$w_eff[$i]/$w_itai[$i]<BR>\n";
            }
        }
        print "<BR>\n";
        print "��<INPUT type=\"submit\" name=\"Enter\" value=\"����\">\n";
    } elsif ($Command eq "DEATHGET") {  #���Υ����ƥදå
        local($itno) = -1;
        for ($i=0; $i<5; $i++) {
            if ($item[$i] eq "�ʤ�") {
                $itno = $i ;
            }
        }
        print "����å���ޤ�����<BR><BR>\n";
        print "��<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>���<BR><BR>\n";
        print "<INPUT TYPE=\"HIDDEN\" NAME=\"Itno\" VALUE=\"$itno\">\n";
        print "<INPUT TYPE=\"HIDDEN\" NAME=\"WId\" VALUE=\"$w_id\">\n";

        if ($w_wep !~ /�Ǽ�/) { #�������
            local($in, $ik) = split(/<>/, $w_wep);
            print "��<INPUT type=\"radio\" name=\"Command\" value=\"GET_6\">$in/$w_watt/$w_wtai<BR>\n";
        }
        if ($w_bou !~ /����/) { #�ɶ�����
            local($in, $ik) = split(/<>/, $w_bou);
            print "��<INPUT type=\"radio\" name=\"Command\" value=\"GET_7\">$in/$w_bdef/$w_btai<BR>\n";
        }
        if ($w_bou_h !~ /�ʤ�/) { #�ɶ�����
            local($in, $ik) = split(/<>/, $w_bou_h);
            print "��<INPUT type=\"radio\" name=\"Command\" value=\"GET_8\">$in/$w_bdef_h/$w_btai_h<BR>\n";
        }
        if ($w_bou_f !~ /�ʤ�/) { #�ɶ�����
            local($in, $ik) = split(/<>/, $w_bou_f);
            print "��<INPUT type=\"radio\" name=\"Command\" value=\"GET_9\">$in/$w_bdef_f/$w_btai_f<BR>\n";
        }
        if ($w_bou_a !~ /�ʤ�/) { #�ɶ�����
            local($in, $ik) = split(/<>/, $w_bou_a);
            print "��<INPUT type=\"radio\" name=\"Command\" value=\"GET_10\">$in/$w_bdef_a/$w_btai_a<BR>\n";
        }

        for ($i=0; $i<6; $i++) {
            if ($w_item[$i] ne "�ʤ�") {
                local($in, $ik) = split(/<>/, $w_item[$i]);
                print "��<INPUT type=\"radio\" name=\"Command\" value=\"GET_$i\">$in/$w_eff[$i]/$w_itai[$i]<BR>\n";
            }
        }
        print "<BR>\n";
        print "��<INPUT type=\"submit\" name=\"Enter\" value=\"����\">\n";
    } elsif ($Command eq "POISON") {    #��ʪ����
        $log = ($log . "���������򺮤���С������դդա�<BR>") ;
        print "������ʪ�������ޤ�����<BR><BR>\n";
        print "��<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>���<BR><BR>\n";
        for ($i=0; $i<5; $i++) {
            if ($item[$i] =~ /<>SH|<>HH|<>SD|<>HD/) {
                local($in, $ik) = split(/<>/, $item[$i]);
                print "��<INPUT type=\"radio\" name=\"Command\" value=\"POI_$i\">$in/$eff[$i]/$itai[$i]<BR>\n";
            }
        }
        print "<BR>\n";
        print "��<INPUT type=\"submit\" name=\"Enter\" value=\"����\">\n";
    } elsif ($Command eq "PSCHECK") {   #�Ǹ�
        $log = ($log . "��������������Ƥ��ʤ���Ĵ�٤Ƥߤ褦��������<BR>") ;
        print "�����Ǹ��򤷤ޤ�����<BR><BR>\n";
        print "��<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>���<BR><BR>\n";
        for ($i=0; $i<5; $i++) {
            if ($item[$i] =~ /<>SH|<>HH|<>SD|<>HD/) {
                local($in, $ik) = split(/<>/, $item[$i]);
                print "��<INPUT type=\"radio\" name=\"Command\" value=\"PSC_$i\">$in/$eff[$i]/$itai[$i]<BR>\n";
            }
        }
        print "<BR>\n";
        print "��<INPUT type=\"submit\" name=\"Enter\" value=\"����\">\n";
    } elsif ($Command eq "SPIICH") { #���ӥ��ԡ�������
        $log = ($log . "�����Ȥ��С��ߤ�ʤ�ʹ������Ȧ���ʡ�����<BR>") ;
        print "���ӥ��ԡ�����Ȥäơ������������������ޤ���<BR>\n";
        print "�����ѣ���ʸ���ޤǡ�<BR><BR>\n";
        print "��<INPUT size=\"30\" type=\"text\" name=\"speech\"maxlength=\"50\"><BR><BR>\n";
        print "��<INPUT type=\"radio\" name=\"Command\" value=\"SPEAKER\">������<BR>\n";
        print "��<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>�ߤ��<BR><BR>\n";
        print "��<INPUT type=\"submit\" name=\"Enter\" value=\"����\">\n";
    } elsif ($Command eq "WINCHG") {    #�����ѹ�
        $log = ($log . "����������˴���θ��ʤ��ѹ����ޤ���<BR>") ;
        print "���ʤ����Ϥ��Ƥ�������<BR>\n";
        print "�����ѣ���ʸ���ޤǡ�<BR><BR>\n";
        print "��������<BR>\n";
        print "��<INPUT size=\"30\" type=\"text\" name=\"Message\" maxlength=\"64\" value=\"$msg\"><BR><BR>\n";
        print "�����<BR>\n";
        print "��<INPUT size=\"30\" type=\"text\" name=\"Message2\" maxlength=\"64\" value=\"$dmes\"><BR><BR>\n";
        print "��������ȡ�<BR>\n";
        print "��<INPUT size=\"30\" type=\"text\" name=\"Comment\" maxlength=\"64\" value=\"$com\"><BR><BR>\n";
        print "��<INPUT type=\"submit\" name=\"Enter\" value=\"����\">\n";
    } elsif ($Command eq "ITMAIN") {    #�����ƥ�
        $log = ($log . "�ǥ��ѥå�����ˤϡ��������äƤ������ʡ�������<BR>") ;
        print "����Ԥ��ޤ�����<BR><BR>\n";
        print "��<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>���<BR><BR>\n";
        print "��<INPUT type=\"radio\" name=\"Command\" value=\"ITEM\">�����ƥ���ѡ�����<BR>\n";
        print "��<INPUT type=\"radio\" name=\"Command\" value=\"DEL\">�����ƥ����<BR>\n";
        print "��<INPUT type=\"radio\" name=\"Command\" value=\"SEIRI\">�����ƥ�����<BR>\n";
        print "��<INPUT type=\"radio\" name=\"Command\" value=\"GOUSEI\">�����ƥ����<BR>\n";
        if ($wep ne "�Ǽ�<>WP") {
            print "��<INPUT type=\"radio\" name=\"Command\" value=\"WEPDEL\">�������򳰤�<BR>\n";
            print "��<INPUT type=\"radio\" name=\"Command\" value=\"WEPDEL2\">����������<BR>\n";
        }
        print "<BR>\n";
        print "��<INPUT type=\"submit\" name=\"Enter\" value=\"����\">\n";
    } elsif ($Command eq "SPECIAL") {   #�ü�
        $log = ($log . "�ü쥳�ޥ�ɤǤ���<BR>") ;
        print "����Ԥ��ޤ�����<BR><BR>\n";
        print "��<select name=\"Command\">\n" ;
        print "��<option value=\"MAIN\" selected>���</option>\n";
        print "��<option value=\"DEFCHK\">������ǧ</option>\n";
        print "��<option value=\"WINCHG\">�����ѹ�</option>\n";
        print "��<option value=\"WEPPNT\">������٥��ǧ</option>\n";
        print "��<option value=\"OUKYU\">���޽���</option>\n";
        if ($club eq "����������" ) { print "��<option value=\"PSCHECK\">�Ǹ�</option>\n"; }
        for ($poi=0; $poi<5; $poi++){
            if ($item[$poi] eq "����<>Y") {
                print "��<option value=\"POISON\">��ʪ����</option>\n";
                last;
            }
        }
        for ($spi=0; $spi<5; $spi++){
            if ($item[$spi] eq "���ӥ��ԡ���<>Y") {
                print "��<option value=\"SPIICH\">���ԡ�������</option>\n";
                last;
            }
        }
        for ($paso=0; $paso<5; $paso++){
            if (($item[$paso] eq "��Х���PC<>Y")&&($itai[$paso] >= 1)) {
                print "��<option value=\"HACK\">�ϥå���</option>\n";
                last;
            }
        }

        print "</select><BR>\n" ;
        print "<BR>\n";
        print "��<INPUT type=\"submit\" name=\"Enter\" value=\"����\">\n";
    } elsif ($Command eq "USRSAVE") {   #�桼���ǡ�����¸
        &u_save;
    } else {
        print "����Ԥ��ޤ�����<BR><BR>\n";
        print "��<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>���<BR><BR>\n";
        print "��<INPUT type=\"submit\" name=\"Enter\" value=\"����\">\n";
    }


}
#====================#
# �� �桼��������¸  #
#====================#
sub SAVE {


    open(DB,"$user_file");seek(DB,0,0); @userlist=<DB>;close(DB);

    $chksts = "NG";
    for ($i=0; $i<$#userlist+1; $i++) {
        ($w_i,$w_p,$a) = split(/,/, $userlist[$i]);
        if (($id2 eq $w_i) && ($password2 eq $w_p)) {   #ID���ס�
            $chksts = "OK";$Index=$i;last;
        }
    }

    if ($chksts eq "OK") {
        if ($hit <= 0) {
            $userlist[$Index] = "$id,$password,$f_name,$l_name,$sex,$cl,$no,$endtime,$att,$def,$hit,$mhit,$level,$exp,$sta,$wep,$watt,$wtai,$bou,$bdef,$btai,$bou_h,$bdef_h,$btai_h,$bou_f,$bdef_f,$btai_f,$bou_a,$bdef_a,$btai_a,$tactics,$death,$msg,$sts,$pls,$kill,$icon,$item[0],$eff[0],$itai[0],$item[1],$eff[1],$itai[1],$item[2],$eff[2],$itai[2],$item[3],$eff[3],$itai[3],$item[4],$eff[4],$itai[4],$item[5],$eff[5],$itai[5],,$dmes,$bid,$club,$wn,$wp,$wa,$wg,$we,$wc,$wd,$wb,$wf,$ws,$com,$inf,\n" ;
        } else {
            $userlist[$Index] = "$id,$password,$f_name,$l_name,$sex,$cl,$no,$endtime,$att,$def,$hit,$mhit,$level,$exp,$sta,$wep,$watt,$wtai,$bou,$bdef,$btai,$bou_h,$bdef_h,$btai_h,$bou_f,$bdef_f,$btai_f,$bou_a,$bdef_a,$btai_a,$tactics,$death,$msg,$sts,$pls,$kill,$icon,$item[0],$eff[0],$itai[0],$item[1],$eff[1],$itai[1],$item[2],$eff[2],$itai[2],$item[3],$eff[3],$itai[3],$item[4],$eff[4],$itai[4],$item[5],$eff[5],$itai[5],,$dmes,$bid,$club,$wn,$wp,$wa,$wg,$we,$wc,$wd,$wb,$wf,$ws,$com,$inf,\n" ;
        }
        open(DB,">$user_file"); seek(DB,0,0); print DB @userlist; close(DB);
    }


}
#====================#
# �� Ũ������¸      #
#====================#
sub SAVE2 {


    open(DB,"$user_file");seek(DB,0,0); @userlist=<DB>;close(DB);

    if ($w_hit <= 0) { $w_sts = "��˴"; }
    $userlist[$Index2] = "$w_id,$w_password,$w_f_name,$w_l_name,$w_sex,$w_cl,$w_no,$w_endtime,$w_att,$w_def,$w_hit,$w_mhit,$w_level,$w_exp,$w_sta,$w_wep,$w_watt,$w_wtai,$w_bou,$w_bdef,$w_btai,$w_bou_h,$w_bdef_h,$w_btai_h,$w_bou_f,$w_bdef_f,$w_btai_f,$w_bou_a,$w_bdef_a,$w_btai_a,$w_tactics,$w_death,$w_msg,$w_sts,$w_pls,$w_kill,$w_icon,$w_item[0],$w_eff[0],$w_itai[0],$w_item[1],$w_eff[1],$w_itai[1],$w_item[2],$w_eff[2],$w_itai[2],$w_item[3],$w_eff[3],$w_itai[3],$w_item[4],$w_eff[4],$w_itai[4],$w_item[5],$w_eff[5],$w_itai[5],$w_log,$w_dmes,$w_bid,$w_club,$w_wn,$w_wp,$w_wa,$w_wg,$w_we,$w_wc,$w_wd,$w_wb,$w_wf,$w_ws,$w_com,$w_inf,\n" ;

    open(DB,">$user_file"); seek(DB,0,0); print DB @userlist; close(DB);


}

#====================#
# �� ���å����ɹ�    #
#====================#
sub CREAD {
    local($xx, $name, $value);
    for $xx (split(/; */, $ENV{'HTTP_COOKIE'})) {
        if ($xx =~ /BR/){
            $cooks = $xx;
            $cooks =~ s/BR=//;
            $cooks =~ s/([0-9A-Fa-f][0-9A-Fa-f])/pack("C", hex($1))/eg;
            ($c_id,$c_password,$c_f_name,$c_l_name,$c_sex,$c_cl,$c_no,$c_endtime,$c_att,$c_def,$c_hit,$c_mhit,$c_level,$c_exp,$c_sta,$c_wep,$c_watt,$c_wtai,$c_bou,$c_bdef,$c_btai,$c_bou_h,$c_bdef_h,$c_btai_h,$c_bou_f,$c_bdef_f,$c_btai_f,$c_bou_a,$c_bdef_a,$c_btai_a,$c_tactics,$c_death,$c_msg,$c_sts,$c_pls,$c_kill,$c_icon,$c_item[0],$c_eff[0],$c_itai[0],$c_item[1],$c_eff[1],$c_itai[1],$c_item[2],$c_eff[2],$c_itai[2],$c_item[3],$c_eff[3],$c_itai[3],$c_item[4],$c_eff[4],$c_itai[4],$c_item[5],$c_eff[5],$c_itai[5],$c_log,$c_dmes,$c_bid,$c_club,$c_wn,$c_wp,$c_wa,$c_wg,$c_we,$c_wc,$c_wd,$c_wb,$c_wf,$c_ws,$c_com,$c_inf,$c_f_name_y,$c_l_name_y,$c_koma) = split(/,/, $cooks);
        }
    }
}

#====================#
# �� ���å�����¸    #
#====================#
sub CSAVE {
    $cook = "$id,$password,$f_name,$l_name,$sex,$cl,$no,0,$att,$def,$hit,$mhit,$level,$exp,$sta,$wep,$watt,$wtai,$bou,$bdef,$btai,$bou_h,$bdef_h,$btai_h,$bou_f,$bdef_f,$btai_f,$bou_a,$bdef_a,$btai_a,$tactics,$death,$msg,$sts,$pls,$kill,$icon,$item[0],$eff[0],$itai[0],$item[1],$eff[1],$itai[1],$item[2],$eff[2],$itai[2],$item[3],$eff[3],$itai[3],$item[4],$eff[4],$itai[4],$item[5],$eff[5],$itai[5],,$dmes,$bid,$club,$wn,$wp,$wa,$wg,$we,$wc,$wd,$wb,$wf,$ws,$com,$inf,";
    $cook =~ s/(.)/sprintf("%02X", unpack("C", $1))/eg;
    print "Set-Cookie: BR=$cook; expires=$expires\n";
}

#====================#
# �� ���å������    #
#====================#
sub CDELETE {
    $cook = ",,,,,,,$now,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,";
    $cook =~ s/(.)/sprintf("%02X", unpack("C", $1))/eg;
    print "Set-Cookie: BR=$cook; expires=$expires\n";
}

#====================#
# �� ��ά�׻�        #
#====================#
sub TACTGET {

    $chkpnt = 5 ;   #Ũ�������ƥ�ȯ��Ψ
    $chkpnt2 = 5 ;  #��������Ψ
    $atp = 1.00 ;
    $dfp = 1.00 ;

    if ($arsts[$pls] eq "WU") { #������
        $atp+=0.2 ;
    } elsif ($arsts[$pls] eq "WD") {    #���⸺
        $atp-=0.2 ;
    } elsif ($arsts[$pls] eq "DU") {    #�ɸ���
        $dfp+=0.2 ;
    } elsif ($arsts[$pls] eq "DD") {    #�ɸ渺
        $dfp-=0.2 ;
    } elsif ($arsts[$pls] eq "SU") {    #ȯ����
        $chkpnt+=2 ;
    } elsif ($arsts[$pls] eq "SD") {    #ȯ����
        $chkpnt-=2 ;
    }

    if ($inf =~ /��/) { $atp -= 0.2; }

    local($kind) = $w_kind ;
    local($wmei) = 0;
    local($wweps) = "" ;

    if (($kind =~ /B/) || (($kind =~ /G|A/) && ($wtai == 0))) { #���� or ��̵���� or ��̵����
        $wweps = "S" ;
        $wmei = 80 ;
        $wmei += int($wb/$BASE);
    } elsif ($kind =~ /A/) {        #��
        $wweps = "L" ;
        $wmei = 60 ;
        $wmei += int($wa/$BASE);
    }elsif ($kind =~ /C/) { #��
        $wweps = "L" ;
        $wmei = 70 ;
        $wmei += int($wc/$BASE);
    }elsif ($kind =~ /D/) { #��
        $wweps = "L" ;
        $wmei = 50 ;
        $wmei += int($wd/$BASE);
    }elsif ($kind =~ /G/) { #��
        $wweps = "L" ;
        $wmei = 50 ;
        $wmei += int($wg/$BASE);
    }elsif ($kind =~ /N/) { #��
        $wweps = "S" ;
        $wmei = 80 ;
        $wmei += int($wn/$BASE);
    }elsif ($kind  =~ /S/) {    #��
        $wweps = "S" ;
        $wmei = 80 ;
        $wmei += int($ws/$BASE);
    } else {    #��
        $wweps = "S" ;
        $wmei = 70 ;
        $wmei += int($wp/$BASE);
    }

    $weps = $wweps ;
    $mei = $wmei ;

    if ($inf =~ /Ƭ/) { $mei -= 20; }
}
#====================#
# �� ��ά�׻�        #
#====================#
sub TACTGET2 {

    $atn = 1.00 ;
    $dfn = 1.00 ;
    $sen = 1.0 ;

    if ($arsts[$w_pls] eq "WU") {   #������
        $atn+=0.2 ;
    } elsif ($arsts[$w_pls] eq "WD") {  #���⸺
        $atn-=0.2 ;
    } elsif ($arsts[$w_pls] eq "DU") {  #�ɸ���
        $dfn+=0.2 ;
    } elsif ($arsts[$w_pls] eq "DD") {  #�ɸ渺
        $dfn-=0.2 ;
    }

    if ($w_inf =~ /��/) { $atn -= 0.2; }

    local($kind) = $w_kind2 ;
    local($wmei) = 0;
    local($wweps) = "" ;

    if (($kind =~ /B/) || (($kind =~ /G|A/) && ($w_wtai == 0))) { #���� or ��̵���� or ��̵����
        $wweps = "S" ;
        $wmei = 80 ;
        $wmei += int($wb/$BASE);
    } elsif ($kind =~ /A/) {        #��
        $wweps = "L" ;
        $wmei = 60 ;
        $wmei += int($wa/$BASE);
    }elsif ($kind =~ /C/) { #��
        $wweps = "L" ;
        $wmei = 70 ;
        $wmei += int($wc/$BASE);
    }elsif ($kind =~ /D/) { #��
        $wweps = "L" ;
        $wmei = 50 ;
        $wmei += int($wd/$BASE);
    }elsif ($kind =~ /G/) { #��
        $wweps = "L" ;
        $wmei = 50 ;
        $wmei += int($wg/$BASE);
    }elsif ($kind =~ /N/) { #��
        $wweps = "S" ;
        $wmei = 80 ;
        $wmei += int($wn/$BASE);
    }elsif ($kind  =~ /S/) {    #��
        $wweps = "S" ;
        $wmei = 80 ;
        $wmei += int($ws/$BASE);
    } else {    #��
        $wweps = "S" ;
        $wmei = 70 ;
        $wmei += int($wp/$BASE);
    }

    $weps2 = $wweps ;
    $mei2 = $wmei ;

    if ($w_inf =~ /Ƭ/) { $mei2 -= 20; }
}

#====================#
# �� �����ߥ��ڤ�    #
#====================#
sub DRAIN{
    local($d_mode) = $_[0];
    $log = ($log . "$l_name�ϡ������ߥʤ��Ԥ���������������HP������������<BR>") ;
    $sta = $maxsta ;
    local($dhit) = int(rand(($mhit/100)*20)+(($mhit/100)*10));
    if ($dhit <= 0) { $dhit = 1 ;}
    $mhit -= $dhit;
    if ($mhit <= 0) {
        $hit = $mhit = 0;
        $log = ($log . "<font color=\"red\"><b>$f_name $l_name��$cl $sex$no�֡ˤϻ�˴������</b></font><br>") ;
            &LOGSAVE("DEATH") ; #��˴��
            $mem--; if ($mem == 1) {&LOGSAVE("WINEND1") ;}
        if($d_mode eq "mov"){
            &SAVE;return;
        }elsif($d_mode eq "eve"){
            $Command = "EVENT";
        }
    } elsif ($hit > $mhit) { $hit = $mhit ; }
}

#=============================#
# �� �桼��ñ�̤Υǡ��������� #
#=============================#
sub u_save{
    local($u_dat) = "$id,$password,$f_name,$l_name,$sex,$cl,$no,$endtime,$att,$def,$hit,$mhit,$level,$exp,$sta,$wep,$watt,$wtai,$bou,$bdef,$btai,$bou_h,$bdef_h,$btai_h,$bou_f,$bdef_f,$btai_f,$bou_a,$bdef_a,$btai_a,$tactics,$death,$msg,$sts,$pls,$kill,$icon,$item[0],$eff[0],$itai[0],$item[1],$eff[1],$itai[1],$item[2],$eff[2],$itai[2],$item[3],$eff[3],$itai[3],$item[4],$eff[4],$itai[4],$item[5],$eff[5],$itai[5],,$dmes,$bid,$club,$wn,$wp,$wa,$wg,$we,$wc,$wd,$wb,$wf,$ws,$com,$inf,\n" ;

    open(DB,">$u_save_dir$id$u_save_file"); seek(DB,0,0); print DB $u_dat; close(DB);

    $log = ($log . "�����֤�����˽�λ���ޤ�����<BR>") ;
    print "<br>��<INPUT type=\"radio\" name=\"Command\" value=\"MAIN\" checked>���<BR><BR>\n";
    print "��<INPUT type=\"submit\" name=\"Enter\" value=\"����\">\n";
    return ;

}

1
