#==================#
# �� �����ƥ�����  #
#==================#
sub ITEMBUNKATU {

    local($wk) = $Command;
    $wk =~ s/BUNKATU_//g;
    local($in, $ik) = split(/<>/, $item[$wk]);

    $j = $Command2;

    if (($item[$wk] eq "�ʤ�") || ($j < 1)) {
        &ERROR("�����ʥ��������Ǥ���");
    }

    local($chk) = "NG" ;
    for ($wk2=0; $wk2<5; $wk2++) {
        if ($item[$wk2] eq "�ʤ�") {
            $chk = "ON" ; last;
        }
    }

    if ($chk eq "NG") {
        $log = ($log . "����ʾ�ǥ��ѥå�������ޤ���<br>") ;
    } elsif (($ik =~ /HH|HD|SH|SD/) && ($j < $itai[$wk])) { # ���������ƥ�
        $itai[$wk] = $itai[$wk] - $j;
        $itai[$wk2] = $j;
        $item[$wk2] = $item[$wk]; $eff[$wk2] = $eff[$wk];
        $log = $log . "$in��ʬ�䤷�ޤ�����<br>";
    } elsif (($ik =~ /W/) && ($ik =~ /C|D/) && ($itai[$wk] ne "��") && ($j < $itai[$wk])) { # ���������
        $itai[$wk] = $itai[$wk] - $j;
        $itai[$wk2] = $j;
        $item[$wk2] = $item[$wk]; $eff[$wk2] = $eff[$wk];
        $log = $log . "$in��ʬ�䤷�ޤ�����<br>";
    } elsif (($ik eq "Y") && ($in =~ /����|ţ/) && ($j < $itai[$wk])) {  # ��ﶯ�������ƥ�
        $itai[$wk] = $itai[$wk] - $j;
        $itai[$wk2] = $j;
        $item[$wk2] = $item[$wk]; $eff[$wk2] = $eff[$wk];
        $log = $log . "$in��ʬ�䤷�ޤ�����<br>";
    } elsif (($ik eq "Y") && ($in =~ /����|�����º�/) && ($j < $itai[$wk])) {    # �Ǵط�
        $itai[$wk] = $itai[$wk] - $j;
        $itai[$wk2] = $j;
        $item[$wk2] = $item[$wk]; $eff[$wk2] = $eff[$wk];
        $log = $log . "$in��ʬ�䤷�ޤ�����<br>";
    } elsif (($ik eq "Y") && ($in =~ /����ƻ��/) && ($j < $itai[$wk])) { # ����ƻ��
        $itai[$wk] = $itai[$wk] - $j;
        $itai[$wk2] = $j;
        $item[$wk2] = $item[$wk]; $eff[$wk2] = $eff[$wk];
        $log = $log . "$in��ʬ�䤷�ޤ�����<br>";
    } elsif (($ik eq "Y") && ($in =~ /��|��/) && ($j < $eff[$wk])) { # �ƴݡ���
        $eff[$wk] = $eff[$wk] - $j;
        $eff[$wk2] = $j;
        $item[$wk2] = $item[$wk]; $itai[$wk2] = $itai[$wk];
        $log = $log . "$in��ʬ�䤷�ޤ�����<br>";
    } elsif (($ik eq "Y") && ($in =~ /�Хåƥ�/) && ($j < $itai[$wk])) { # �Хåƥ�
        $itai[$wk] = $itai[$wk] - $j;
        $itai[$wk2] = $j;
        $item[$wk2] = $item[$wk]; $eff[$wk2] = $eff[$wk];
        $log = $log . "$in��ʬ�䤷�ޤ�����<br>";
    } else { # ʬ��Ǥ��ʤ�ʪ����
        $log = $log . "ʬ�伺�ԡ�<br>";
    }

    $Command = "MAIN";
    $Command2 = "";

    &SAVE;

}
1
