#==================#
# �� �����ƥ����  #
#==================#
sub ITEMGOUSEI {

    $wk = $Command;
    $wk =~ s/GOUSEI_//g;
    ($in, $ik) = split(/<>/, $item[$wk]);

    $wk2 = $Command2;
    $wk2 =~ s/GOUSEI2_//g;
    ($in2, $ik2) = split(/<>/, $item[$wk2]);

    if (($item[$wk] eq "�ʤ�")||($item[$wk2] eq "�ʤ�")) {
        &ERROR("�����ʥ��������Ǥ���");
    }

    $chk = "NG" ;

    if(($itai[$wk] == 1)||($itai[$wk] eq "��")){
        $chk = "ON"; $itai[$wk] == 1;$j=$wk;
    }elsif($ik =~ /DB|DH|DF|DA/){
        $chk = "ON"; ;$j=$wk;
    }elsif(($itai[$wk2] == 1)||($itai[$wk2] eq "��")){
        $chk = "ON"; $itai[$wk2] == 1;$j=$wk2;
    }elsif($ik2 =~ /DB|DH|DF|DA/){
        $chk = "ON"; ;$j=$wk2;
    }else{
        for ($j=0; $j<5; $j++) {
            if ($item[$j] eq "�ʤ�") {
                $chk = "ON" ; last;
            }
        }
    }

    if ($chk eq "NG") {
        $log = ($log . "����ʾ�ǥ��ѥå�������ޤ���<br>") ;
    } else {
        $log = ($log . "�����ƥ��������ޤ���<br>") ;
        if (($wk == $wk2)||($in eq $in2)) { #Ʊ�����ƥ�����
            $log = ($log . "$in��į��Ƥߤ���<br>") ;
        }else{
            require "$g_table";

            #�ơ��֥����
            local($k) = 0;
            local($l) = $#g_item1+1;
            for ($k=0; $k<$l; $k++) {
                $gousei{"$g_item1[$k]"}{"$g_item2[$k]"}{"name"} = "$g_name[$k]";
                $gousei{"$g_item1[$k]"}{"$g_item2[$k]"}{"kind"} = "$g_kind[$k]";
                $gousei{"$g_item1[$k]"}{"$g_item2[$k]"}{"eff"}  = "$g_eff[$k]";
                $gousei{"$g_item1[$k]"}{"$g_item2[$k]"}{"itai"} = "$g_itai[$k]";
            }

            if($gousei{$in}{$in2}{name}){ #�����ơ��֥���ѹ���
                $log = ($log . "$in��$in2��$gousei{$in}{$in2}{name}�����褿��<BR>");
                $item[$j] = "$gousei{$in}{$in2}{name}<>$gousei{$in}{$in2}{kind}";
                $eff[$j] = $gousei{$in}{$in2}{eff} ;
                $itai[$j] = $gousei{$in}{$in2}{itai} ;
                &ITEMCOUNT;
            }elsif($gousei{$in2}{$in}{name}){ #�����ơ��֥���ѹ���(��)
                $log = ($log . "$in��$in2��$gousei{$in2}{$in}{name}�����褿��<BR>");
                $item[$j] = "$gousei{$in2}{$in}{name}<>$gousei{$in2}{$in}{kind}";
                $eff[$j] = $gousei{$in2}{$in}{eff} ;
                $itai[$j] = $gousei{$in2}{$in}{itai} ;
                &ITEMCOUNT;
            }else { #�㤦�����ƥࡦ�����Ǥ��ʤ�ʪ����
                $log = ($log . "$in��$in2���Ȥ߹�碌���ʤ��ʡ�<br>") ;
            }
        }
    }

    $Command = "MAIN";
    $Command2 = "";

    &SAVE;

}

sub ITEMCOUNT{
    if($wk == $j){
        if($ik2 =~ /DB|DH|DF|DA/){
            $item[$wk2] = "�ʤ�"; $eff[$wk2] = 0; $itai[$wk2] = 0 ;
        }else{
            $itai[$wk2] -= 1;
            if ($itai[$wk2] <= 0) {$item[$wk2] = "�ʤ�"; $eff[$wk2] = 0; $itai[$wk2] = 0 ;}
        }
    }elsif($wk2 == $j){
        if($ik =~ /DB|DH|DF|DA/){
            $item[$wk] = "�ʤ�"; $eff[$wk] = 0; $itai[$wk] = 0 ;
        }else{
            $itai[$wk] -= 1;
            if ($itai[$wk] <= 0) {$item[$wk] = "�ʤ�"; $eff[$wk] = 0; $itai[$wk] = 0 ;}
        }
    }else{
        if($ik =~ /DB|DH|DF|DA/){
            $item[$wk] = "�ʤ�"; $eff[$wk] = 0; $itai[$wk] = 0 ;
        }else{
            $itai[$wk] -= 1;
            if ($itai[$wk] <= 0) {$item[$wk] = "�ʤ�"; $eff[$wk] = 0; $itai[$wk] = 0 ;}
        }
        if($ik2 =~ /DB|DH|DF|DA/){
            $item[$wk2] = "�ʤ�"; $eff[$wk2] = 0; $itai[$wk2] = 0 ;
        }else{
            $itai[$wk2] -= 1;
            if ($itai[$wk2] <= 0) {$item[$wk2] = "�ʤ�"; $eff[$wk2] = 0; $itai[$wk2] = 0 ;}
        }
    }
}

1
