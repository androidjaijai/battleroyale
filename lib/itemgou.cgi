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

    $log = ($log . "�����ƥ��������ޤ���<br>") ;
    if (($wk == $wk2)||($in eq $in2)) { #Ʊ�����ƥ�����
        $log = ($log . "$in��į��Ƥߤ���<br>") ;
    }else{
        require "$g_table";

        if($gousei{$in}{$in2}) { #�����ơ��֥���ѹ���
            local($w_item,$w_eff,$w_itai,$type) = split(/,/, $gousei{$in}{$in2});
            local($w_in,$w_ik) = split(/<>/, $w_item);

            if($w_eff eq "k1") { $w_eff = $eff[$wk]; }
            elsif($w_eff eq "k2") { $w_eff = $eff[$wk2]; }
            elsif($w_eff eq "k3") { $w_eff = $eff[$wk] + $eff[$wk2]; }

            if($w_itai eq "k1") { $w_itai = $itai[$wk]; }
            elsif($w_itai eq "k2") { $w_itai = $itai[$wk2]; }
            elsif($w_itai eq "k3") { $w_itai = $itai[$wk] + $itai[$wk2]; }

            if($type == 0) {
                $log = ($log . "$in��$in2��$w_in�����褿��<BR>");
                $item[$wk] = $w_item; $eff[$wk] = $w_eff; $itai[$wk] = $w_itai;
                $item[$wk2] = "�ʤ�"; $eff[$wk2] = 0; $itai[$wk2] = 0;
            } elsif($type == 1) {
                $log = ($log . "$in��$in2��$w_in�����褿��<BR>");
                $item[$wk] = $w_item; $eff[$wk] = $w_eff; $itai[$wk] = $w_itai;
                $itai[$wk2]--;
                if ($itai[$wk2] <= 0) { $item[$wk2] = "�ʤ�"; $eff[$wk2] = 0; $itai[$wk2] = 0; }
            } elsif($type == 2) {
                $log = ($log . "$in��$in2��$w_in�����褿��<BR>");
                $item[$wk2] = $w_item; $eff[$wk2] = $w_eff; $itai[$wk2] = $w_itai;
                $itai[$wk]--;
                if ($itai[$wk] <= 0) { $item[$wk] = "�ʤ�"; $eff[$wk] = 0; $itai[$wk] = 0; }
            } else {
                $chk = "NG" ;
                if($itai[$wk] == 1) {
                    $chk = "ON"; $j=$wk;
                } elsif($itai[$wk2] == 1) {
                    $chk = "ON"; $j=$wk2;
                } else {
                    for ($j=0; $j<5; $j++) {
                        if ($item[$j] eq "�ʤ�") { $chk = "ON" ; last; }
                    }
                }

                if ($chk eq "NG") {
                    $log = ($log . "����ʾ�ǥ��ѥå�������ޤ���<br>") ;
                } else {
                    $log = ($log . "$in��$in2��$w_in�����褿��<BR>");
                    $itai[$wk]--; if ($itai[$wk] <= 0) { $item[$wk] = "�ʤ�"; $eff[$wk] = 0; $itai[$wk] = 0; }
                    $itai[$wk2]--; if ($itai[$wk2] <= 0) { $item[$wk2] = "�ʤ�"; $eff[$wk2] = 0; $itai[$wk2] = 0; }
                    $item[$j] = $w_item; $eff[$j] = $w_eff; $itai[$j] = $w_itai;
                }
            }
        } elsif($gousei{$in2}{$in}) { #�����ơ��֥���ѹ���(��)
            local($w_item,$w_eff,$w_itai,$type) = split(/,/, $gousei{$in2}{$in});
            local($w_in,$w_ik) = split(/<>/, $w_item);

            if($w_eff eq "k1") { $w_eff = $eff[$wk2]; }
            elsif($w_eff eq "k2") { $w_eff = $eff[$wk]; }
            elsif($w_eff eq "k3") { $w_eff = $eff[$wk] + $eff[$wk2]; }

            if($w_itai eq "k1") { $w_itai = $itai[$wk2]; }
            elsif($w_itai eq "k2") { $w_itai = $itai[$wk]; }
            elsif($w_itai eq "k3") { $w_itai = $itai[$wk] + $eff[$wk2]; }

            if($type == 0) {
                $log = ($log . "$in��$in2��$w_in�����褿��<BR>");
                $item[$wk] = $w_item; $eff[$wk] = $w_eff; $itai[$wk] = $w_itai;
                $item[$wk2] = "�ʤ�"; $eff[$wk2] = 0; $itai[$wk2] = 0;
            } elsif($type == 1) {
                $log = ($log . "$in��$in2��$w_in�����褿��<BR>");
                $item[$wk2] = $w_item; $eff[$wk2] = $w_eff; $itai[$wk2] = $w_itai;
                $itai[$wk]--;
                if ($itai[$wk] <= 0) { $item[$wk] = "�ʤ�"; $eff[$wk] = 0; $itai[$wk] = 0; }
            } elsif($type == 2) {
                $log = ($log . "$in��$in2��$w_in�����褿��<BR>");
                $item[$wk] = $w_item; $eff[$wk] = $w_eff; $itai[$wk] = $w_itai;
                $itai[$wk2]--;
                if ($itai[$wk2] <= 0) { $item[$wk2] = "�ʤ�"; $eff[$wk2] = 0; $itai[$wk2] = 0; }
            } elsif($type == 3) {
                $chk = "NG" ;
                if($itai[$wk] == 1) {
                    $chk = "ON"; $j=$wk;
                } elsif($itai[$wk2] == 1) {
                    $chk = "ON"; $j=$wk2;
                } else {
                    for ($j=0; $j<5; $j++) {
                        if ($item[$j] eq "�ʤ�") { $chk = "ON" ; last; }
                    }
                }

                if ($chk eq "NG") {
                    $log = ($log . "����ʾ�ǥ��ѥå�������ޤ���<br>") ;
                } else {
                    $log = ($log . "$in��$in2��$w_in�����褿��<BR>");
                    $itai[$wk]--; if ($itai[$wk] <= 0) { $item[$wk] = "�ʤ�"; $eff[$wk] = 0; $itai[$wk] = 0; }
                    $itai[$wk2]--; if ($itai[$wk2] <= 0) { $item[$wk2] = "�ʤ�"; $eff[$wk2] = 0; $itai[$wk2] = 0; }
                    $item[$j] = $w_item; $eff[$j] = $w_eff; $itai[$j] = $w_itai;
                }
            }
        } elsif(($ik =~ /��/) && ($ik2 =~ /��/)) { #�������
            $chk = "NG" ;
            if($itai[$wk] == 1) {
                $chk = "ON"; $j=$wk;
            } elsif($itai[$wk2] == 1) {
                $chk = "ON"; $j=$wk2;
            } else {
                for ($j=0; $j<5; $j++) {
                    if ($item[$j] eq "�ʤ�") { $chk = "ON" ; last; }
                }
            }

            if ($chk eq "NG") {
                $log = ($log . "����ʾ�ǥ��ѥå�������ޤ���<br>") ;
            } else {
                $log = ($log . "$in��$in2��$f_name�������������褿��<BR>");
                $itai[$wk]--; if ($itai[$wk] <= 0) { $item[$wk] = "�ʤ�"; $eff[$wk] = 0; $itai[$wk] = 0; }
                $itai[$wk2]--; if ($itai[$wk2] <= 0) { $item[$wk2] = "�ʤ�"; $eff[$wk2] = 0; $itai[$wk2] = 0; }

                if(int(rand(2))==0) { $item[$j] = "$f_name��������<>SH"; }
                else { $item[$j] = "$f_name��������<>HH"; }

                if ($club ne "����������") {
                    if(($ik =~ /HD|SD/) || ($ik2 =~ /HD|SD/)) {
                        $item[$j] =~ s/<>HH/<>HD/g;
                        $item[$j] =~ s/<>SH/<>SD/g;
                    } elsif(int(rand(3))==0) {
                        $log = ($log . "�����������Τ����٤ƤϤʤ�ʤ�ʪ���ä��褦�ʵ��������<BR>");
                        $item[$j] =~ s/<>HH/<>HD/g;
                        $item[$j] =~ s/<>SH/<>SD/g;
                    }
                }
                $eff[$j] = int(rand(21)+20);
                $itai[$j] = int(rand(2)+1);
            }
        } else { #�㤦�����ƥࡦ�����Ǥ��ʤ�ʪ����
            $log = ($log . "$in��$in2���Ȥ߹�碌���ʤ��ʡ�<br>") ;
        }
    }

    $Command = "MAIN";
    $Command2 = "";

    &SAVE;

}

1
