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
        if($item[$wk] =~ /<>H.*/){
            $item[$wk] =~ s/<>H.*/<>HD2/g;
        }else{ $item[$wk] =~ s/<>S.*/<>SD2/g; }
    } else {
        if($item[$wk] =~ /<>HH/){
            $item[$wk] =~ s/<>HH/<>HD/g;
        }else{ $item[$wk] =~ s/<>SH/<>SD/g; }
    }
    &SAVE ;
    $Command = "MAIN" ;
}
#==================#
# �� �Ǹ�����      #
#==================#
sub PSCHECK {

    local($wk) = $Command;
    $wk =~ s/PSC_//g;
    if (($item[$wk] !~ /<>SH|<>HH|<>SD|<>HD/)||($club ne "����������" )) {
        &ERROR("�����ʥ��������Ǥ���");
    }
    
    local($in, $ik) = split(/<>/, $item[$wk]);
    if ($ik =~ /SH|HH/) {
        $log = ($log . "�� $in �� ���ˤ��Ƥ������������������<br>") ;
    } else {
        $log = ($log . "�� $in �ˤ� ��ʪ���������Ƥ��ꤽ������������<br>") ;
    }
    $sta -= $dokumi_sta ;
    if ($sta <= 0) {    #�����ߥ��ڤ졩
        &DRAIN("com");
    }
    &SAVE ;
    $Command = "MAIN" ;
}

1
