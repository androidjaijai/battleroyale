#=====================#
# �� ���ӥ��ԡ������� #
#=====================#
sub SPEAKER {
    for ($i=0; $i<5; $i++){
        if ($item[$i] =~ /���ӥ��ԡ���/) {
            last;
        }
    }
    if ($item[$i] !~ /���ӥ��ԡ���/) {
        &ERROR("�����ʥ��������Ǥ���");
    }

    $log = ($log . " $speech<BR>");
    $log = ($log . " ����������ä����ʡ�<BR>");
    open(DB,"$gun_log_file");seek(DB,0,0); @gunlog=<DB>;close(DB);
    $namae = "$f_name $l_name" ;
    $gunlog[2] = "$now,$place[$pls],$namae,$speech,\n";
    open(DB,">$gun_log_file"); seek(DB,0,0); print DB @gunlog; close(DB);

    $Command = "MAIN" ;

}
1