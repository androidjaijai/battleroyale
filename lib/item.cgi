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
            if (($item[$i] eq "�ʤ�") || (($item[$i] eq $getitem) && ($getitem =~ /<>WC|<>TN|<>NR|�ƴ�|��/))) {
                $chkflg = $i;last;
            }
        }

        if ($getitem =~ /<>TO/) { #�
            open(DB,">$filename"); seek(DB,0,0); print DB @itemlist; close(DB);

            $result = int(rand($geteff/2)+($geteff/2));
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
            }elsif ($item[$chkflg] =~ /�ƴ�|��/) {
                $eff[$chkflg] += $geteff;
            } else {
                $itai[$chkflg] += $gettai ;
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
            $result = int($eff[$wk]*1.5) ;
        } else { $result = $eff[$wk] ; }
        $hit -= $result ;
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
    } elsif(($item[$wk] =~ /<>W/) && ($item[$wk] !~ /<>WF/)) {  #�������
        $log = ($log . "$in������������<BR>") ;
        $wep2 = $wep; $watt2 = $watt; $wtai2 = $wtai ;
        $wep = $item[$wk]; $watt = $eff[$wk]; $wtai = $itai[$wk] ;
        if ($wep2 !~ /�Ǽ�/) {
            $item[$wk] = $wep2; $eff[$wk] = $watt2; $itai[$wk] = $wtai2 ;
        } else {
            $item[$wk] = "�ʤ�"; $eff[$wk] = 0; $itai[$wk] = 0 ;
        }
    } elsif($item[$wk] =~ /<>DB/) { #�ɶ��������Ρ�
        $log = ($log . "$in���Τ�����������<BR>");
        $bou2 = $bou; $bdef2 = $bdef; $btai2 = $btai ;
        $bou = $item[$wk]; $bdef = $eff[$wk]; $btai = $itai[$wk] ;
        if ($bou2 !~ /����/) {
            $item[$wk] = $bou2; $eff[$wk] = $bdef2; $itai[$wk] = $btai2 ;
        } else {
            $item[$wk] = "�ʤ�"; $eff[$wk] = 0; $itai[$wk] = 0 ;
        }
    } elsif($item[$wk] =~ /<>DH/) { #�ɶ�������Ƭ��
        $log = ($log . "$in��Ƭ������������<BR>");
        $bou2 = $bou_h; $bdef2 = $bdef_h; $btai2 = $btai_h ;
        $bou_h = $item[$wk]; $bdef_h = $eff[$wk]; $btai_h = $itai[$wk] ;
        if ($bou2 !~ /�ʤ�/) {
            $item[$wk] = $bou2; $eff[$wk] = $bdef2; $itai[$wk] = $btai2 ;
        } else {
            $item[$wk] = "�ʤ�"; $eff[$wk] = 0; $itai[$wk] = 0 ;
        }
    } elsif($item[$wk] =~ /<>DF/) { #�ɶ�������­��
        $log = ($log . "$in��­������������<BR>");
        $bou2 = $bou_f; $bdef2 = $bdef_f; $btai2 = $btai_f ;
        $bou_f = $item[$wk]; $bdef_f = $eff[$wk]; $btai_f = $itai[$wk] ;
        if ($bou2 !~ /�ʤ�/) {
            $item[$wk] = $bou2; $eff[$wk] = $bdef2; $itai[$wk] = $btai2 ;
        } else {
            $item[$wk] = "�ʤ�"; $eff[$wk] = 0; $itai[$wk] = 0 ;
        }
    } elsif($item[$wk] =~ /<>DA/) { #�ɶ��������ӡ�
        $log = ($log . "$in���Ӥ�����������<BR>");
        $bou2 = $bou_a; $bdef2 = $bdef_a; $btai2 = $btai_a ;
        $bou_a = $item[$wk]; $bdef_a = $eff[$wk]; $btai_a = $itai[$wk] ;
        if ($bou2 !~ /�ʤ�/) {
            $item[$wk] = $bou2; $eff[$wk] = $bdef2; $itai[$wk] = $btai2 ;
        } else {
            $item[$wk] = "�ʤ�"; $eff[$wk] = 0; $itai[$wk] = 0 ;
        }
    } elsif($item[$wk] =~ /<>A/) {  #��������������
        $log = ($log . "$in��Ȥ��դ�����<BR>");
        $bou2 = $item[5]; $bdef2 = $eff[5]; $btai2 = $itai[5] ;
        $item[5] = $item[$wk]; $eff[5] = $eff[$wk]; $itai[5] = $itai[$wk] ;
        if ($bou2 !~ /�ʤ�/) {
            $item[$wk] = $bou2; $eff[$wk] = $bdef2; $itai[$wk] = $btai2 ;
        } else {
            $item[$wk] = "�ʤ�"; $eff[$wk] = 0; $itai[$wk] = 0 ;
        }
    } elsif($item[$wk] =~ /<>R/) {  #�졼����
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
    } elsif((($in eq "����")||($in eq "�ۤ���")) && ($wep =~ /<>WN/)) { #���л��ѡ��ʥ��շ�������
        $watt += $eff[$wk]; if ($watt > 30) { $watt = 30 ; }
        $log = ($log . "$in����Ѥ�����$w_name�ι����Ϥ� $watt �ˤʤä���<BR>");
        $itai[$wk] -- ;
        if ($itai[$wk] <= 0) {$item[$wk] = "�ʤ�"; $eff[$wk] = 0; $itai[$wk] = 0 ;}
    } elsif(($in eq "��˥ƻ��") && ($d_kind eq "DBN") && ($d_name ne "����")) { #��˥ƻ�������������
        $btai += $eff[$wk]; if ($btai > 30) { $btai = 30 ; }
        $log = ($log . "$in����Ѥ�����$d_name���ѵ��Ϥ� $btai �ˤʤä���<BR>");
        $itai[$wk] -- ;
        if ($itai[$wk] <= 0) {$item[$wk] = "�ʤ�"; $eff[$wk] = 0; $itai[$wk] = 0 ;}
    } elsif(($in eq "�ƴ�") && ($wep =~ /<>WG/)) {  #�ƴݻ��ѡ��Ʒ�������
        $up = $eff[$wk] + $wtai;if ($up > 6) { $up = 6 - $wtai ; } else { $up = $eff[$wk]; }
        $wtai += $up ; $eff[$wk] -= $up ;
        if ($eff[$wk] <= 0) {$item[$wk] = "�ʤ�"; $eff[$wk] = 0; $itai[$wk] = 0 ;}
        if ($wep =~ /<>WGB/) { $wep =~ s/<>WGB/<>WG/g ; }
        $log = ($log . "$in��$w_name ����Ŷ������<BR>$w_name�λ��Ѳ���� $up ���夷����<BR>");
    } elsif(($in =~ /��/) && ($wep =~ /<>WA/)) {    #����ѡ��ݷ�������
        $up = $eff[$wk] + $wtai;if ($up > 6) { $up = 6 - $wtai ; }else { $up = $eff[$wk]; }
        $wtai += $up ; $eff[$wk] -= $up ;
        if ($eff[$wk] <= 0) {$item[$wk] = "�ʤ�"; $eff[$wk] = 0; $itai[$wk] = 0 ;}
        if ($wep =~ /<>WAB/) { $wep =~ s/<>WAB/<>WA/g ; }
        $log = ($log . "$in����Ѥ���$w_name���佼������<BR>$w_name�λ��Ѳ���� $up ���夷����<BR>");
    } elsif($in =~ /�Хåƥ�/){
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

    local($wk) = $Command;
    $wk =~ s/DEL_//g;

    if ($item[$wk] eq "�ʤ�") {
        &ERROR("�����ʥ��������Ǥ���");
    }

    local($in, $ik) = split(/<>/, $item[$wk]);

    $log = ($log . "$in��ΤƤ���<br>") ;

    local($filename) = "$LOG_DIR/$pls$item_file";
    open(DB,"$filename");seek(DB,0,0); @itemlist=<DB>;close(DB);
    push(@itemlist,"$item[$wk],$eff[$wk],$itai[$wk],\n") ;
    open(DB,">$filename"); seek(DB,0,0); print DB @itemlist; close(DB);

    $item[$wk] = "�ʤ�"; $eff[$wk] = 0; $itai[$wk] = 0 ;
    $Command = "MAIN";

    &SAVE;

}
#==================#
# �� ������ﳰ������  #
#==================#
sub WEPDEL {

    local($j) = 0 ;

    if ($wep =~ /�Ǽ�/) {
        $log = ($log . "$l_name�������������Ƥ��ޤ���<br>") ;
        $Command = "MAIN" ;
        return ;
    }

    ($w_name,$w_kind) = split(/<>/, $wep);

    local($chk) = "NG" ;
    for ($j=0; $j<5; $j++) {
        if ($item[$j] eq "�ʤ�") {
            $chk = "ON" ; last;
        }
    }

    if ($chk eq "NG") {
        $log = ($log . "����ʾ�ǥ��ѥå�������ޤ���<br>") ;
    } else {
        $log = ($log . "$w_name��ǥ��ѥå��ˤ��ޤ��ޤ�����<br>") ;
        $item[$j] = $wep; $eff[$j] = $watt; $itai[$j] = $wtai ;
        $wep = "�Ǽ�<>WP"; $watt = 0; $wtai = "��" ;
        &SAVE ;
    }

    $Command = "MAIN" ;

}
#==================#
# �� ����������  #
#==================#
sub WEPDEL2 {

    if ($wep =~ /�Ǽ�/) {
        $log = ($log . "$l_name�������������Ƥ��ޤ���<br>") ;
        $Command = "MAIN" ;
        return ;
    }

    local($in, $ik) = split(/<>/, $wep);

    $log = ($log . "$in��ΤƤ���<br>") ;

    local($filename) = "$LOG_DIR/$pls$item_file";
    open(DB,"$filename");seek(DB,0,0); @itemlist=<DB>;close(DB);
    push(@itemlist,"$wep,$watt,$wtai,\n") ;
    open(DB,">$filename"); seek(DB,0,0); print DB @itemlist; close(DB);

    $wep = "�Ǽ�<>WP"; $watt = 0; $wtai = "��" ;
    $Command = "MAIN";

    &SAVE;

}
1