#==================#
# �� �����ƥ����  #
#==================#
sub ITEMGET {

    local($i) = 0 ;
    local($chkflg) = -1;
    local($sub) = "";

    local($filename) = "$LOG_DIR/$pls$item_file";


    open(DB,"$filename");seek(DB,0,0); @itemlist=<DB>;close(DB);

    if ($#itemlist < 0) {
        $log = ($log . "�⤦�����Υ��ꥢ�ˤϲ���̵���Τ��ʡ�������<BR>") ;
        $chksts="OK";
        return ;
    } else {
        local($work) = int(rand($#itemlist)) ;
        local($getitem,$geteff,$gettai) = split(/,/, $itemlist[$work]) ;
        local($itname,$itkind) = split(/<>/, $getitem);
        local($delitem) = splice(@itemlist,$work,1) ;
        for ($i=0; $i<5; $i++) {
            if ($item[$i] eq "�ʤ�") {
                $chkflg = $i;last;
            } elsif (($item[$i] eq $getitem) && ($getitem =~ /<>TN|�ƴ�|��/)) {
                $chkflg = $i;last;
            } elsif (($item[$i] eq $getitem) && ($getitem =~ /<>WC|<>WD/) && ($itai[$i] ne "��")) {
                $chkflg = $i;last;
            }
        }

        if ($getitem =~ /<>TO/) { #�
            open(DB,">$filename"); seek(DB,0,0); print DB @itemlist; close(DB);

            $result = int(rand($geteff * 0.4)+($geteff * 0.8));
            $log = ($log . "櫤����ųݤ����Ƥ��� $itname �ǽ��򤪤���<font color=\"red\"><b>$result�Υ��᡼��</b></font>�����������<BR>") ;
            $hit-=$result;
            if ($hit <= 0) {
                $hit = 0;
                $log = ($log . "<font color=\"red\"><b>$f_name $l_name��$cl $sex$no�֡ˤϻ�˴������</b></font><br>") ;
                #��˴��
                &LOGSAVE("DEATH") ;
                $mem--;
                if ($mem == 1) {&LOGSAVE("WINEND1") ;}
            }
            return ;
        }

        if ($chkflg == -1) { #����ʥ����С�
            $log = ($log . "$itname��ȯ��������������������ʾ奫�Х������ʤ���<BR>$itname�򤢤���᤿��������<BR>") ;
            $Command = "MAIN";
        } else {
            open(DB,">$filename"); seek(DB,0,0); print DB @itemlist; close(DB);

            if($getitem =~ /<>HH|<>HD/) {
                $sub = "���ˤ�������Ϥ��������褽�����ʡ�";
            } elsif($getitem =~ /<>SH|<>SD/) {
                $sub = "���ˤ���Х����ߥʤ��������褽�����ʡ�";
            } elsif ($getitem =~ /<>W/) { #��
                $sub = "�����Ĥ����ˤʤꤽ�����ʡ�";
            } elsif($getitem =~ /<>D/) { #�ɶ�
                $sub = "�����Ĥ��ɶ�˽��褽�����ʡ�";
            } elsif($getitem =~ /<>A/) { #����
                $sub = "�����ĤϿȤ��դ��뤳�Ȥ����褽�����ʡ�";
            } elsif($getitem =~ /<>TN/) { #�
                $sub = "�����櫤�ųݤ���������褽�����ʡ�";
            } else {
                $sub = "���äȲ����˻Ȥ��������";
            }

            ($itname,$kind) = split(/<>/, $getitem) ;
            $log = ($log . "$itname��ȯ��������$sub<BR>") ;

            if ($item[$chkflg] eq "�ʤ�") {
                $item[$chkflg] = $getitem; $eff[$chkflg] = $geteff; $itai[$chkflg] = $gettai;
            } elsif ($item[$chkflg] =~ /�ƴ�|��/) {
                $eff[$chkflg] += $geteff;
            } else {
                if ($item[$chkflg] =~ /<>WC|<>WD/) {
                    $eff[$chkflg] = int(($eff[$chkflg]*$itai[$chkflg] + $geteff*$gettai) / ($itai[$chkflg]+$gettai));
                }
                $itai[$chkflg] += $gettai;
            }
        }
    }
    $chksts="OK";

}
#==================#
# �� �����ƥ����  #
#==================#
sub ITEM {

    local($result) = 0;
    local($wep2) = "" ;
    local($watt2) = 0;
    local($wtai2) = 0 ;
    local($up) = 0 ;

    local($wk) = $Command;
    $wk =~ s/ITEM_//g;

    if ($item[$wk] eq "�ʤ�") {
        &ERROR("�����ʥ��������Ǥ���");
    }

    local($in, $ik) = split(/<>/, $item[$wk]);
    local($w_name,$w_kind) = split(/<>/, $wep);
    local($d_name,$d_kind) = split(/<>/, $bou);
    local($d_name_h,$d_kind_h) = split(/<>/, $bou_h);
    local($d_name_a,$d_kind_a) = split(/<>/, $bou_a);
    local($d_name_f,$d_kind_f) = split(/<>/, $bou_f);

    if ($item[$wk] =~ /<>SH/) { #�����ߥʲ���
        $log = ($log . "$in����Ѥ�����<BR>�����ߥʤ���������<BR>");
        $sta += $eff[$wk] ;
        if ($sta > $maxsta) {$sta = $maxsta;}
        $itai[$wk] --;
        if ($itai[$wk] == 0) {$item[$wk] = "�ʤ�"; $eff[$wk] = 0; $itai[$wk] = 0 ; }
    } elsif($item[$wk] =~ /<>HH/) { #���ϲ���
        $log = ($log . "$in����Ѥ�����<BR>���Ϥ���������<BR>");
        $hit += $eff[$wk] ;
        if ($hit > $mhit) {$hit = $mhit;}
        $itai[$wk] --;
        if ($itai[$wk] == 0) {$item[$wk] = "�ʤ�"; $eff[$wk] = 0; $itai[$wk] = 0 ; }
    } elsif($item[$wk] =~ /<>SD|<>HD/) {    #������
        if ($item[$wk] =~ /<>SD2|<>HD2/) {  #����������������
            $result = int($eff[$wk]*1.5);
        } else {
            $result = $eff[$wk];
        }
        $hit -= $result ;
        $inf =~ s/��//g ;
        $inf = ($inf . "��") ;
        $log = ($log . "���á��������ޤä����ɤ���顢��ʪ����������Ƥ����ߤ�������<font color=\"red\"><b>$result���᡼��</b></font>��<BR>\n") ;
        $itai[$wk] --;
        if ($itai[$wk] == 0) {$item[$wk] = "�ʤ�"; $eff[$wk] = 0; $itai[$wk] = 0 ; }
        if ($hit <= 0) {
            $log = ($log . "<font color=\"red\"><b>$f_name $l_name��$cl $sex$no�֡ˤϻ�˴������</b></font><br>\n") ;
            $com = int(rand(6)) ;
            #��˴��
            &LOGSAVE("DEATH1") ;
            $mem--;
            if ($mem == 1) { &LOGSAVE("WINEND1"); }
            &SAVE;return;
        }
    } elsif ($item[$wk] =~ /<>W/) {  #�������
        if ($ik =~ /��/) {
            $inf =~ s/��//g ;
            $inf = ($inf . "��") ;
        }
        if (($in eq "�Х�ơ���") && ($w_name eq "�Х�ơ���")) {
            $watt += $eff[$wk]; if ($watt > 25) { $watt = 25 ; }
            $log = ($log . "$in��Ťͤƴ�������$w_name�ι����Ϥ� $watt �ˤʤä���<BR>");
            $item[$wk] = "�ʤ�"; $eff[$wk] = 0; $itai[$wk] = 0 ;
        } else {
            $log = ($log . "$in������������<BR>") ;
            $wep2 = $wep; $watt2 = $watt; $wtai2 = $wtai ;
            $wep = $item[$wk]; $watt = $eff[$wk]; $wtai = $itai[$wk] ;
            if ($wep2 !~ /�Ǽ�/) {
                $item[$wk] = $wep2; $eff[$wk] = $watt2; $itai[$wk] = $wtai2 ;
            } else {
                $item[$wk] = "�ʤ�"; $eff[$wk] = 0; $itai[$wk] = 0 ;
            }
        }
    } elsif ($item[$wk] =~ /<>DB/) { #�ɶ��������Ρ�
        if ($ik =~ /��/) {
            $inf =~ s/��//g ;
            $inf = ($inf . "��") ;
        }
        $log = ($log . "$in���Τ�����������<BR>");
        $bou2 = $bou; $bdef2 = $bdef; $btai2 = $btai ;
        $bou = $item[$wk]; $bdef = $eff[$wk]; $btai = $itai[$wk] ;
        if ($bou2 ne "����<>DN") {
            $item[$wk] = $bou2; $eff[$wk] = $bdef2; $itai[$wk] = $btai2 ;
        } else {
            $item[$wk] = "�ʤ�"; $eff[$wk] = 0; $itai[$wk] = 0 ;
        }
    } elsif($item[$wk] =~ /<>DH/) { #�ɶ�������Ƭ��
        if ($ik =~ /��/) {
            $inf =~ s/��//g ;
            $inf = ($inf . "��") ;
        }
        $log = ($log . "$in��Ƭ������������<BR>");
        $bou2 = $bou_h; $bdef2 = $bdef_h; $btai2 = $btai_h ;
        $bou_h = $item[$wk]; $bdef_h = $eff[$wk]; $btai_h = $itai[$wk] ;
        if ($bou2 ne "�ʤ�") {
            $item[$wk] = $bou2; $eff[$wk] = $bdef2; $itai[$wk] = $btai2 ;
        } else {
            $item[$wk] = "�ʤ�"; $eff[$wk] = 0; $itai[$wk] = 0 ;
        }
    } elsif($item[$wk] =~ /<>DF/) { #�ɶ�������­��
        if ($ik =~ /��/) {
            $inf =~ s/��//g ;
            $inf = ($inf . "��") ;
        }
        $log = ($log . "$in��­������������<BR>");
        $bou2 = $bou_f; $bdef2 = $bdef_f; $btai2 = $btai_f ;
        $bou_f = $item[$wk]; $bdef_f = $eff[$wk]; $btai_f = $itai[$wk] ;
        if ($bou2 ne "�ʤ�") {
            $item[$wk] = $bou2; $eff[$wk] = $bdef2; $itai[$wk] = $btai2 ;
        } else {
            $item[$wk] = "�ʤ�"; $eff[$wk] = 0; $itai[$wk] = 0 ;
        }
    } elsif($item[$wk] =~ /<>DA/) { #�ɶ��������ӡ�
        if ($ik =~ /��/) {
            $inf =~ s/��//g ;
            $inf = ($inf . "��") ;
        }
        $log = ($log . "$in���Ӥ�����������<BR>");
        $bou2 = $bou_a; $bdef2 = $bdef_a; $btai2 = $btai_a ;
        $bou_a = $item[$wk]; $bdef_a = $eff[$wk]; $btai_a = $itai[$wk] ;
        if ($bou2 ne "�ʤ�") {
            $item[$wk] = $bou2; $eff[$wk] = $bdef2; $itai[$wk] = $btai2 ;
        } else {
            $item[$wk] = "�ʤ�"; $eff[$wk] = 0; $itai[$wk] = 0 ;
        }
    } elsif($item[$wk] =~ /<>A/) {  #��������������
        if ($ik =~ /��/) {
            $inf =~ s/��//g ;
            $inf = ($inf . "��") ;
        }
        $log = ($log . "$in��Ȥ��դ�����<BR>");
        $bou2 = $item[5]; $bdef2 = $eff[5]; $btai2 = $itai[5] ;
        $item[5] = $item[$wk]; $eff[5] = $eff[$wk]; $itai[5] = $itai[$wk] ;
        if ($bou2 ne "�ʤ�") {
            $item[$wk] = $bou2; $eff[$wk] = $bdef2; $itai[$wk] = $btai2 ;
        } else {
            $item[$wk] = "�ʤ�"; $eff[$wk] = 0; $itai[$wk] = 0 ;
        }
    } elsif($item[$wk] =~ /<>R/) {  #�졼����
        $log = ($log . "�졼��������Ѥ�����<BR><BR>���������ꥢ�ˤ���Ϳ�<BR>�ֿ�������ʬ�����륨�ꥢ�οͿ�");
        &HEADER;
        require "$LIB_DIR/reader.cgi";
        &READER;
        &FOOTER;
    } elsif($item[$wk] =~ /<>TN/) { #�
        $log = ($log . "$in��櫤Ȥ��ƻųݤ�������ʬ����դ��ʤ���ʡ�������<BR>");

        $item[$wk] =~ s/TN/TO/g ;

        $filename = "$LOG_DIR/$pls$item_file";

        open(DB,"$filename");seek(DB,0,0); @itemlist=<DB>;close(DB);
        push(@itemlist,"$item[$wk],$eff[$wk],$itai[$wk],\n") ;
        open(DB,">$filename"); seek(DB,0,0); print DB @itemlist; close(DB);
        $itai[$wk] -- ;
        $item[$wk] =~ s/TO/TN/g ;
        if ($itai[$wk] <= 0) {$item[$wk] = "�ʤ�"; $eff[$wk] = 0; $itai[$wk] = 0 ;}
    } elsif(($in eq "����") && ($w_kind =~ /N|S/)) { #���л��ѡ���or�ɷ�������
        if($wep =~ /���ɤ�/) {
            $watt -= 10 - $eff[$wk]; if ($watt > 30) { $watt = 30 ; }
            $wep =~ s/���ɤ�//g;
            $log = ($log . "���ޤä���$in���Ǥ���Ȥ��Ƥ��ޤä���$w_name�ι����Ϥ� $watt �ˤʤä���������<BR>");
        } else {
            $watt += $eff[$wk]; if ($watt > 30) { $watt = 30 ; }
            $log = ($log . "$in����Ѥ�����$w_name�ι����Ϥ� $watt �ˤʤä���<BR>");
        }
        $itai[$wk] -- ;
        if ($itai[$wk] <= 0) {$item[$wk] = "�ʤ�"; $eff[$wk] = 0; $itai[$wk] = 0 ;}
    } elsif(($in eq "����") && ($w_kind =~ /N|S/)) { #�������ѡ��·�or�ɷ�������
        $watt += $eff[$wk]; if ($watt > 40) { $watt = 40 ; }
        if($wep !~ /��/) { $wep = ("���ɤ�" . $wep); }
        $log = ($log . "$in����Ѥ�����$w_name�ι����Ϥ� $watt �ˤʤä���<BR>");
        $itai[$wk] -- ;
        if ($itai[$wk] <= 0) {$item[$wk] = "�ʤ�"; $eff[$wk] = 0; $itai[$wk] = 0 ;}
    } elsif(($in eq "ţ") && ($w_kind =~ /B/) && ($w_kind !~ /G|A/)) { #ţ���ѡ�����������
        $watt += $eff[$wk]; if ($watt > 30) { $watt = 30 ; }
        if($wep !~ /ţ/) { $wep = ("ţ�դ�" . $wep); }
        $log = ($log . "$in����Ѥ�����$w_name�ι����Ϥ� $watt �ˤʤä���<BR>");
        $itai[$wk] -- ;
        if ($itai[$wk] <= 0) {$item[$wk] = "�ʤ�"; $eff[$wk] = 0; $itai[$wk] = 0 ;}
    } elsif (($in eq "����ƻ��[��]") && ($d_name ne "����")) { #���ɶ�������
        $btai += $eff[$wk]; if ($btai > 30) { $btai = 30 ; }
        $log = ($log . "$in����Ѥ�����$d_name���ѵ��Ϥ� $btai �ˤʤä���<BR>");
        $itai[$wk] -- ;
        if ($itai[$wk] <= 0) {$item[$wk] = "�ʤ�"; $eff[$wk] = 0; $itai[$wk] = 0 ;}
    } elsif (($in eq "����ƻ��[Ƭ]") && ($d_name_h ne "�ʤ�")) { #Ƭ�ɶ�������
        $btai_h += $eff[$wk]; if ($btai_h > 20) { $btai_h = 20 ; }
        $log = ($log . "$in����Ѥ�����$dh_name���ѵ��Ϥ� $btai_h �ˤʤä���<BR>");
        $itai[$wk] -- ;
        if ($itai[$wk] <= 0) {$item[$wk] = "�ʤ�"; $eff[$wk] = 0; $itai[$wk] = 0 ;}
    } elsif (($in eq "����ƻ��[��]") && ($d_name_a ne "�ʤ�")) { #���ɶ�������
        $btai_a += $eff[$wk]; if ($btai_a > 20) { $btai_a = 20 ; }
        $log = ($log . "$in����Ѥ�����$da_name���ѵ��Ϥ� $btai_a �ˤʤä���<BR>");
        $itai[$wk] -- ;
        if ($itai[$wk] <= 0) {$item[$wk] = "�ʤ�"; $eff[$wk] = 0; $itai[$wk] = 0 ;}
    } elsif (($in eq "����ƻ��[­]") && ($d_name_f ne "�ʤ�")) { #­�ɶ�������
        $btai_f += $eff[$wk]; if ($btai_f > 20) { $btai_f = 20 ; }
        $log = ($log . "$in����Ѥ�����$df_name���ѵ��Ϥ� $btai_f �ˤʤä���<BR>");
        $itai[$wk] -- ;
        if ($itai[$wk] <= 0) {$item[$wk] = "�ʤ�"; $eff[$wk] = 0; $itai[$wk] = 0 ;}
    } elsif(($in eq "�ƴ�") && ($wep =~ /<>WG/)) {  #�ƴݻ��ѡ��Ʒ�������
        $up = $eff[$wk] + $wtai;if ($up > 12) { $up = 12 - $wtai ; } else { $up = $eff[$wk]; }
        $wtai += $up ; $eff[$wk] -= $up ;
        if ($eff[$wk] <= 0) {$item[$wk] = "�ʤ�"; $eff[$wk] = 0; $itai[$wk] = 0 ;}
        $log = ($log . "$in��$w_name ����Ŷ������<BR>$w_name�λ��Ѳ���� $up ���夷����<BR>");
    } elsif(($in eq "��") && ($wep =~ /<>WA/)) {    #����ѡ��ݷ�������
        $up = $eff[$wk] + $wtai;if ($up > 12) { $up = 12 - $wtai ; }else { $up = $eff[$wk]; }
        $wtai += $up ; $eff[$wk] -= $up ;
        if ($eff[$wk] <= 0) {$item[$wk] = "�ʤ�"; $eff[$wk] = 0; $itai[$wk] = 0 ;}
        $log = ($log . "$in��$w_name ���佼������<BR>$w_name�λ��Ѳ���� $up ���夷����<BR>");
    } elsif($in eq "�Хåƥ�"){
        my($pc_ck) = 0;
        for ($paso=0; $paso<5; $paso++){
            if (($item[$paso] eq "��Х���PC<>Y")&&($itai[$paso] < 5)){
                $itai[$paso] += $eff[$wk];
                if($itai[$paso] > 5){ $itai[$paso] = 5; }
                $itai[$wk] -- ;
                if ($itai[$wk] <= 0) {$item[$wk] = "�ʤ�"; $eff[$wk] = 0; $itai[$wk] = 0 ;}
                $log = ($log . "$in �� ��Х���PC ���Ť�������Х���PC �λ��Ѳ���� $itai[$paso] �ˤʤä���<BR>");
                $pc_ck = 1;
                last;
            }
        }
        if ($pc_ck == 0){
            $log = ($log . "�����Ĥϲ��˻Ȥ��������������<BR>");$Command="MAIN";
        }
    } elsif($in eq "�����κ�") {
        $inf =~ s/��//g ;
        $inf = ($inf . "��") ;
        $log = ($log . "�����������Ƥ椯������<BR><br><font color=\"red\"><b>�������٥ơ������ƥ��ޥ���</b></font><br><br>$l_name�϶����˿����줿��<br>");
        $itai[$wk] -- ;
        if ($itai[$wk] <= 0) {$item[$wk] = "�ʤ�"; $eff[$wk] = 0; $itai[$wk] = 0 ;}
    } elsif($in eq "�ץ����������") {
        if ($pls == 0){
            $inf = ($inf . "��");
            open(FLAG,">$end_flag_file"); print(FLAG "�����λ\n"); close(FLAG);
            &LOGSAVE("EX_END");
            $log = ($log . "���������Ȥäƥץ�������ߤ�����<br>���ؤ����줿��<BR>");$Command="MAIN";
            &SAVE;
        }else{
            $log = ($log . "�����ǻȤäƤ��̣���ʤ���������<BR>");$Command="MAIN";
        }
    } elsif($in eq "��������") {	#�������û���
        $log = ($log . "�������äǼ�������ä�����<BR>�֥����롦���������㡢�⤷�⤷������<BR>$f_name�������äƤ����������ӤϤĤ����ʤ�������$f_name����<BR>��ôǤ�����äˤǤ���������<BR>\n");
    } elsif($in eq "�����") {    #����޻���
        $log = ($log . "����ޤ������������Ƥߤ褦��<BR>\n");
        local($dice) = int(rand(10)) ;
        if ($dice < 5) {
            $log = ($log . "�Ȥ���<BR>�����ϡ��ɸ��Ϥ��夬�ä���<br>\n");
            $att += int(rand(2) + 1) ; $def += int(rand(2) + 1) ;
        } elsif ($dice < 8) {
            $log = ($log . "������<BR>�����ϡ��ɸ��Ϥ������ä���������<br>\n");
            $att -= int(rand(2) + 1) ; $def -= int(rand(2) + 1) ;
        } else {
            $log = ($log . "��Ȥ���<BR>�����ϡ��ɸ��ϡ��������Ϥ��夬�ä�����<br>\n");
            $mhit += int(rand(3)+3) ; $att += int(rand(3)+1); $def += int(rand(3)+1);
        }
        $item[$wk] = "�ʤ�"; $eff[$wk] = 0; $itai[$wk] = 0 ;
    } else {
        $log = ($log . "�����Ĥϲ��˻Ȥ��������������<BR>");$Command="MAIN";
    }

    $Command = "MAIN";

    &SAVE;

}

#==================#
# �� �����ƥ����  #
#==================#
sub ITEMDEL {

    foreach (0 .. $#IDEL) {
        $wk = $IDEL[$_];
        if ($item[$wk] eq "�ʤ�") {
            &ERROR("�����ʥ��������Ǥ���");
        }

        local($in, $ik) = split(/<>/, $item[$wk]);

        $log = ($log . "$in��ΤƤ���<br>") ;

        local($filename) = "$LOG_DIR/$pls$item_file";
        $delitem = "$item[$wk],$eff[$wk],$itai[$wk],\n";
        open(DB,">>$filename"); seek(DB,0,0); print DB $delitem; close(DB);

        $item[$wk] = "�ʤ�"; $eff[$wk] = 0; $itai[$wk] = 0 ;
    }

    $Command = "MAIN";

    &SAVE;

}
#==================#
# �� �����ʲ��    #
#==================#
sub WEPKAI {

    local($wk) = $Command;
    $wk =~ s/WEPKAI2_//g;
    local($j) = 0 ;

    local($chk) = "NG" ;
    for ($j=0; $j<5; $j++) {
        if ($item[$j] eq "�ʤ�") {
            $chk = "ON" ; last;
        }
    }

    if ($chk eq "NG") {
        $log = ($log . "����ʾ�ǥ��ѥå�������ޤ���<br>") ;
    } else {
        if ($wk eq "W") {
            if ($wep eq "�Ǽ�<>WP") {
                $log = ($log . "$l_name�������������Ƥ��ޤ���<br>") ;
                $Command = "MAIN" ;
                return ;
            }

            local($w_name,$w_kind) = split(/<>/, $wep);
            $log = ($log . "$w_name��ǥ��ѥå��ˤ��ޤ��ޤ�����<br>") ;
            $item[$j] = $wep; $eff[$j] = $watt; $itai[$j] = $wtai ;
            $wep = "�Ǽ�<>WP"; $watt = 0; $wtai = "��" ;
        } elsif ($wk eq "B") {
            if ($bou eq "����<>DN") {
                $log = ($log . "$l_name�����ɶ���������Ƥ��ޤ���<br>") ;
                $Command = "MAIN" ;
                return ;
            }

            local($w_name,$w_kind) = split(/<>/, $bou);
            $log = ($log . "$w_name��ǥ��ѥå��ˤ��ޤ��ޤ�����<br>") ;
            $item[$j] = $bou; $eff[$j] = $bdef; $itai[$j] = $btai ;
            $bou = "����<>DN"; $bdef = 0; $btai = "��" ;
        } elsif ($wk eq "H") {
            if ($bou_h eq "�ʤ�") {
                $log = ($log . "$l_name��Ƭ�ɶ���������Ƥ��ޤ���<br>") ;
                $Command = "MAIN" ;
                return ;
            }

            local($w_name,$w_kind) = split(/<>/, $bou_h);
            $log = ($log . "$w_name��ǥ��ѥå��ˤ��ޤ��ޤ�����<br>") ;
            $item[$j] = $bou_h; $eff[$j] = $bdef_h; $itai[$j] = $btai_h ;
            $bou_h = "�ʤ�"; $bdef_h = 0; $btai_h = 0 ;
        } elsif ($wk eq "A") {
            if ($bou_a eq "�ʤ�") {
                $log = ($log . "$l_name�����ɶ���������Ƥ��ޤ���<br>") ;
                $Command = "MAIN" ;
                return ;
            }

            local($w_name,$w_kind) = split(/<>/, $bou_a);
            $log = ($log . "$w_name��ǥ��ѥå��ˤ��ޤ��ޤ�����<br>") ;
            $item[$j] = $bou_a; $eff[$j] = $bdef_a; $itai[$j] = $btai_a ;
            $bou_a = "�ʤ�"; $bdef_a = 0; $btai_a = 0 ;
        } elsif ($wk eq "F") {
            if ($bou_f eq "�ʤ�") {
                $log = ($log . "$l_name��­�ɶ���������Ƥ��ޤ���<br>") ;
                $Command = "MAIN" ;
                return ;
            }

            local($w_name,$w_kind) = split(/<>/, $bou_f);
            $log = ($log . "$w_name��ǥ��ѥå��ˤ��ޤ��ޤ�����<br>") ;
            $item[$j] = $bou_f; $eff[$j] = $bdef_f; $itai[$j] = $btai_f ;
            $bou_f = "�ʤ�"; $bdef_f = 0; $btai_f = 0 ;
        } elsif ($wk eq "I") {
            if ($item[5] eq "�ʤ�") {
                $log = ($log . "$l_name�������ʤ��������Ƥ��ޤ���<br>") ;
                $Command = "MAIN" ;
                return ;
            }

            local($w_name,$w_kind) = split(/<>/, $item[5]);
            $log = ($log . "$w_name��ǥ��ѥå��ˤ��ޤ��ޤ�����<br>") ;
            $item[$j] = $item[5]; $eff[$j] = $eff[5]; $itai[$j] = $itai[5] ;
            $item[5] = "�ʤ�"; $eff[5] = 0; $itai[5] = 0 ;
        }
        &SAVE ;
    }

    $Command = "MAIN" ;

}
#==================#
# �� ���������    #
#==================#
sub WEPDEL {

    local($wk) = $Command;
    $wk =~ s/WEPDEL2_//g;
    local($in, $ik, $delitem);

    if ($wk eq "W") {
        if ($wep eq "�Ǽ�<>WP") {
            $log = ($log . "$l_name�������������Ƥ��ޤ���<br>") ;
            $Command = "MAIN" ;
            return ;
        }

        ($in, $ik) = split(/<>/, $wep);
        $delitem = "$wep,$watt,$wtai,\n";
        $wep = "�Ǽ�<>WP"; $watt = 0; $wtai = "��" ;
    } elsif ($wk eq "B") {
        if ($bou eq "����<>DN") {
            $log = ($log . "$l_name�����ɶ���������Ƥ��ޤ���<br>") ;
            $Command = "MAIN" ;
            return ;
        }

        ($in, $ik) = split(/<>/, $bou);
        $delitem = "$bou,$bdef,$btai,\n";
        $bou = "����<>DN"; $bdef = 0; $btai = "��" ;
    } elsif ($wk eq "H") {
        if ($bou_h eq "�ʤ�") {
            $log = ($log . "$l_name��Ƭ�ɶ���������Ƥ��ޤ���<br>") ;
            $Command = "MAIN" ;
            return ;
        }

        ($in, $ik) = split(/<>/, $bou_h);
        $delitem = "$bou_h,$bdef_h,$btai_h,\n";
        $bou_h = "�ʤ�"; $bdef_h = 0; $btai_h = 0 ;
    } elsif ($wk eq "A") {
        if ($bou_a eq "�ʤ�") {
            $log = ($log . "$l_name�����ɶ���������Ƥ��ޤ���<br>") ;
            $Command = "MAIN" ;
            return ;
        }

        ($in, $ik) = split(/<>/, $bou_a);
        $delitem = "$bou_a,$bdef_a,$btai_a,\n";
        $bou_a = "�ʤ�"; $bdef_a = 0; $btai_a = 0 ;
    } elsif ($wk eq "F") {
        if ($bou_f eq "�ʤ�") {
            $log = ($log . "$l_name��­�ɶ���������Ƥ��ޤ���<br>") ;
            $Command = "MAIN" ;
            return ;
        }

        ($in, $ik) = split(/<>/, $bou_f);
        $delitem = "$bou_f,$bdef_f,$btai_f,\n";
        $bou_f = "�ʤ�"; $bdef_f = 0; $btai_f = 0 ;
    } elsif ($wk eq "I") {
        if ($item[5] eq "�ʤ�") {
            $log = ($log . "$l_name�������ʤ��������Ƥ��ޤ���<br>") ;
            $Command = "MAIN" ;
            return ;
        }

        ($in, $ik) = split(/<>/, $item[5]);
        $delitem = "$item[5],$eff[5],$itai[5],\n";
        $item[5] = "�ʤ�"; $eff[5] = 0; $itai[5] = 0 ;
    } else {
        &ERROR("�����ʥ��������Ǥ���");
    }

    $log = ($log . "$in��ΤƤ���<br>") ;

    local($filename) = "$LOG_DIR/$pls$item_file";
    open(DB,">>$filename"); seek(DB,0,0); print DB $delitem; close(DB);

    $Command = "MAIN";

    &SAVE;

}

#==================#
# �� ���ʬ��      #
#==================#
sub SPLIT {

    local($j) = 0;

    local($chk) = "NG" ;
    if (($wep =~ /<>WG/) && ($wtai > 0)) {
        for ($j=0; $j<5; $j++) {
            if (($item[$j] eq "�ʤ�") || ($item[$j] eq "�ƴ�<>Y")) {
                $chk = "ON" ; last;
            }
        }
        if ($chk eq "NG") {
            $log = ($log . "����ʾ�ǥ��ѥå�������ޤ���<br>") ;
        } else {
            $log = ($log . "�ƴݤ�ǥ��ѥå��ˤ��ޤ��ޤ�����<br>") ;
            $item[$j] ="�ƴ�<>Y"; $eff[$j] += $wtai; $itai[$j] = 1 ;
            $wtai = 0 ;
        }
    } elsif (($wep =~ /<>WA/) && ($wtai > 0)) {
        for ($j=0; $j<5; $j++) {
            if (($item[$j] eq "�ʤ�") || ($item[$j] eq "��<>Y")) {
                $chk = "ON" ; last;
            }
        }
        if ($chk eq "NG") {
            $log = ($log . "����ʾ�ǥ��ѥå�������ޤ���<br>") ;
        } else {
            $log = ($log . "���ǥ��ѥå��ˤ��ޤ��ޤ�����<br>") ;
            $item[$j] ="��<>Y"; $eff[$j] += $wtai; $itai[$j] = 1 ;
            $wtai = 0 ;
        }
    } else {
        local($wn,$wk) = split(/<>/, $wep);
        $log = ($log . "$wn��ʬ��Ǥ��ޤ���<br>") ;
    }

    &SAVE;

    $Command = "MAIN" ;

}
1
