#==================#
# �� ��ʪ��������  #
#==================#
sub POISON {

    for ($i=0; $i<5; $i++) {
        if ($item[$i] =~ /����/) {
            last ;
        }
    }
    local($wk) = $Command;
    $wk =~ s/POI_//g;
    if (($item[$wk] !~ /<>SH|<>HH|<>SD|<>HD/) || ($item[$i] !~ /����/)) {
        &ERROR("�����ʥ��������Ǥ���");
    }
    $itai[$i]--;
    if ($itai[$i] <= 0) {
        $item[$i] = "�ʤ�"; $eff[$i] = $itai[$i] = 0 ;
    }
    local($in, $ik) = split(/<>/, $item[$wk]);
    $log = ($log . "$in����ʪ������������ʬ�Ǹ��ˤ��ʤ��褦����Ĥ��褦��������<br>") ;
    if ($club eq "����������") {
        $item[$wk] =~ s/<>H.*/<>HD2/g;
        $item[$wk] =~ s/<>S.*/<>SD2/g;
    } else {
        $item[$wk] =~ s/<>HH/<>HD/g;
        $item[$wk] =~ s/<>SH/<>SD/g;
    }
    &SAVE ;
    $Command = "MAIN" ;
}
#==================#
# �� �����½���    #
#==================#
sub ANTIPS {

    for ($i=0; $i<5; $i++) {
        if ($item[$i] =~ /�����º�/) {
            last ;
        }
    }
    local($wk) = $Command;
    $wk =~ s/ATPS_//g;
    if (($item[$wk] !~ /<>SH|<>HH|<>SD|<>HD/) || ($item[$i] !~ /�����º�/)) {
        &ERROR("�����ʥ��������Ǥ���");
    }
    $itai[$i]--;
    if ($itai[$i] <= 0) {
        $item[$i] = "�ʤ�"; $eff[$i] = $itai[$i] = 0 ;
    }
    local($in, $ik) = split(/<>/, $item[$wk]);
    $log = ($log . "$in���Ǥ����¤��������������פ�����������<br>") ;
    $item[$wk] =~ s/<>H.*/<>HH/g;
    $item[$wk] =~ s/<>S.*/<>SH/g;

    &SAVE ;
    $Command = "MAIN" ;
}
#==================#
# �� �Ǹ�����      #
#==================#
sub PSCHECK {

    local($wk) = $Command;
    $wk =~ s/PSC_//g;
    if ($item[$wk] !~ /<>SH|<>HH|<>SD|<>HD/) {
        &ERROR("�����ʥ��������Ǥ���");
    }

    local($in, $ik) = split(/<>/, $item[$wk]);
    if ($ik =~ /SH|HH/) {
        $log = ($log . "�� $in �� ���ˤ��Ƥ������������������<br>") ;
    } else {
        $log = ($log . "�� $in �ˤ� ��ʪ���������Ƥ��ꤽ������������<br>") ;
    }

    if ($club eq "����������" ) {
        $sta -= int($dokumi_sta / 2);
    } else {
        $sta -= $dokumi_sta;
    }

    if ($sta <= 0) {    #�����ߥ��ڤ졩
        &DRAIN("com");
    }

    &SAVE ;
    $Command = "MAIN" ;
}

1
