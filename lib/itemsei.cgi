#==================#
# �� �����ƥ����� #
#==================#
sub ITEMSEIRI {

    local($wk) = $Command;
    $wk =~ s/SEIRI_//g;
    local($in, $ik) = split(/<>/, $item[$wk]);

    local($wk2) = $Command2;
    $wk2 =~ s/SEIRI2_//g;
    local($in2, $ik2) = split(/<>/, $item[$wk2]);

    if (($item[$wk] eq "�ʤ�")||($item[$wk2] eq "�ʤ�")) {
        &ERROR("�����ʥ��������Ǥ���");
    }

    $log = ($log . "�����ƥ���������ޤ���<br>") ;

    if ($wk == $wk2) { #Ʊ�����ƥ�����
        $log = ($log . "$in������ľ���ޤ�����<br>") ;
    }elsif (($in eq $in2)&&($eff[$wk] eq $eff[$wk2])&&($ik =~ /HH|HD/)&&($ik2 =~ /HH|HD/)) { #���ϲ��������ƥ�����
        $itai[$wk] = $itai[$wk] + $itai[$wk2];
        if (($ik eq "HD")||($ik2 eq "HD")) {
            $item[$wk] = "$in<>HD";
        }
        if(($ik eq "HD2")||($ik2 eq "HD2")) {
            $item[$wk] = "$in<>HD2";
        }
        $item[$wk2] = "�ʤ�"; $eff[$wk2] = 0; $itai[$wk2] = 0 ;
        $log = ($log . "$in��Ż��ޤ�����<br>") ;
    }elsif (($in eq $in2)&&($eff[$wk] eq $eff[$wk2])&&($ik =~ /SH|SD/)&&($ik2 =~ /SH|SD/)) { #�����ߥʲ��������ƥ�����
            $itai[$wk] = $itai[$wk] + $itai[$wk2];
        if (($ik eq "SD")||($ik2 eq "SD")) {
            $item[$wk] = "$in<>SD";
        }
        if(($ik eq "SD2")||($ik2 eq "SD2")) {
            $item[$wk] = "$in<>SD2";
        }
        $item[$wk2] = "�ʤ�"; $eff[$wk2] = 0; $itai[$wk2] = 0 ;
        $log = ($log . "$in��Ż��ޤ�����<br>") ;
    }elsif (($in eq $in2)&&($ik eq $ik2)&&($ik =~ /W/)&&($ik =~ /C|D/) && ($itai[$wk] ne "��") && ($itai[$wk2] ne "��")) { #��ȯ�������
        $eff[$wk] = int((($eff[$wk] * $itai[$wk]) + ($eff[$wk2] * $itai[$wk2])) / ($itai[$wk] + $itai[$wk2]));
        $itai[$wk] = $itai[$wk] + $itai[$wk2];
        $item[$wk2] = "�ʤ�"; $eff[$wk2] = 0; $itai[$wk2] = 0 ;
        $log = ($log . "$in��Ż��ޤ�����<br>") ;
    }elsif (($in eq $in2)&&($ik eq $ik2)&&($ik eq "Y")&&($in =~ /����|ţ|����/)) { #��ﶯ�������ƥ�
        $eff[$wk] = int((($eff[$wk] * $itai[$wk]) + ($eff[$wk2] * $itai[$wk2])) / ($itai[$wk] + $itai[$wk2]));
        $itai[$wk] = $itai[$wk] + $itai[$wk2];
        $item[$wk2] = "�ʤ�"; $eff[$wk2] = 0; $itai[$wk2] = 0 ;
        $log = ($log . "$in��Ż��ޤ�����<br>") ;
    }elsif (($in eq $in2)&&($ik eq $ik2)&&($ik eq "Y")&&($in =~ /����|�����º�/)) { #�Ǵط�����
        $eff[$wk] = int((($eff[$wk] * $itai[$wk]) + ($eff[$wk2] * $itai[$wk2])) / ($itai[$wk] + $itai[$wk2]));
        $itai[$wk] = $itai[$wk] + $itai[$wk2];
        $item[$wk2] = "�ʤ�"; $eff[$wk2] = 0; $itai[$wk2] = 0 ;
        $log = ($log . "$in��Ż��ޤ�����<br>") ;
    }elsif (($in eq $in2)&&($ik eq $ik2)&&($ik eq "Y")&&($in =~ /����ƻ��/)) { #����ƻ������
        $eff[$wk] = int((($eff[$wk] * $itai[$wk]) + ($eff[$wk2] * $itai[$wk2])) / ($itai[$wk] + $itai[$wk2]));
        $itai[$wk] = $itai[$wk] + $itai[$wk2];
        $item[$wk2] = "�ʤ�"; $eff[$wk2] = 0; $itai[$wk2] = 0 ;
        $log = ($log . "$in��Ż��ޤ�����<br>") ;
    }elsif ((($in eq $in2)&&($ik eq $ik2)&&($ik eq "Y"))&&($in =~ /��|��/)) { #�ƴݡ���
        $eff[$wk] = $eff[$wk] + $eff[$wk2];
        $item[$wk2] = "�ʤ�"; $eff[$wk2] = 0; $itai[$wk2] = 0 ;
        $log = ($log . "$in��Ż��ޤ�����<br>") ;
    }elsif ((($in eq $in2)&&($ik eq $ik2)&&($ik eq "Y"))&&($in =~ /�Хåƥ�/)) { #�Хåƥ�
        $itai[$wk] = $itai[$wk] + $itai[$wk2];
        $item[$wk2] = "�ʤ�"; $eff[$wk2] = 0; $itai[$wk2] = 0 ;
        $log = ($log . "$in��Ż��ޤ�����<br>") ;
    }else { #�㤦�����ƥࡦŻ����ʤ�ʪ����
    $log = ($log . "$in��$in2��Ż����ʤ��ʡ�<br>") ;
    }

    $Command = "MAIN";
    $Command2 = "";

    &SAVE;

}
1
