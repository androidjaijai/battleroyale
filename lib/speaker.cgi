#==================#
# �� ����          #
#==================#
sub SPEAKER {
    if ($club ne "������") {
        for ($i=0; $i<5; $i++){
            if ($item[$i] =~ /���ӥ��ԡ���/) {
                last;
            }
        }
    }
    if (($item[$i] !~ /���ӥ��ԡ���/) && ($club ne "������"))  {
        &ERROR("�����ʥ��������Ǥ���");
    }

    $log = ($log . " $speech<BR>");
    $log = ($log . " ����������ä����ʡ�<BR>");
    open(DB,"$gun_log_file");seek(DB,0,0); @gunlog=<DB>;close(DB);
    $gunlog[2] = "$now,$place[$pls],$f_name $l_name,$speech,\n";
    open(DB,">$gun_log_file"); seek(DB,0,0); print DB @gunlog; close(DB);
    &LOGSAVE("SPEAKER");

    $Command = "MAIN" ;

}
1
