### �ϥå��󥰽��� by kelp###

sub HACKING {

    for ($paso=0; $paso<5; $paso++){
        if (($item[$paso] eq "��Х���PC<>Y") && ($itai[$paso] >= 1)) { last; }
    }

    if (($Command ne "HACK2") || ($item[$paso] ne "��Х���PC<>Y") || ($itai[$paso] <= 0)) {
        &ERROR("�����ʥ��������Ǥ���");
    }

    local($bonus) = 2;  #��������Ψ(0�λ�10%)
    local($dice1) = int(rand(10)) ;
    local($dice2) = int(rand(10)) ;

    if ($club =~ /�ѥ�����/){ #�ѥ��������δ�������Ψ
        $bonus = 5;
    }


    local($kekka) = $bonus;
    if ($dice1 <= $kekka){     #�ϥå�������Ƚ��
        open(DB,"$area_file");seek(DB,0,0); my(@wk_arealist)=<DB>;close(DB);
        my($wk_ar,$wk_hack,$wk_a) = split(/,/, $wk_arealist[1]);  #�ϥå��󥰥ե饰����
        $wk_hack = 1;
        $wk_arealist[1] = "$wk_ar,$wk_hack,,\n";
        open(DB,">$area_file"); seek(DB,0,0); print DB @wk_arealist; close(DB);
        $log = ($log . "�ϥå������������Ƥζػߥ��ꥢ��������줿����<BR>") ;
        &LOGSAVE("HACK");
    }else{
        $log = ($log . "�ϥå��󥰤ϼ��Ԥ���������<BR>") ;
    }

    if ($dice1 >= 9){   #�Хåƥ���ס��ե���֥�������˲�
        $item[$paso] = "�ʤ�"; $eff[$paso] = $itai[$paso] = 0 ;
        $log = ($log . "���Ƥ��ä������ब����Ƥ��ޤä���<BR>") ;
        if ($dice2 >= 9){  #����(��ե���֥�)�����ܤˤ��������ˡ�
            $hit = 0 ; $sts = "��˴"; $death = $deth = "���ܤˤ��跺";$mem--;
            if ($mem == 1) {
                open(FLAG,">$end_flag_file"); print(FLAG "��λ\n"); close(FLAG);
            }
            &LOGSAVE("DEATH5") ;
            open(DB,"$gun_log_file");seek(DB,0,0); @gunlog=<DB>;close(DB);
            $gunlog[1] = "$now,$place[$pls],$id,,\n";
            open(DB,">$gun_log_file"); seek(DB,0,0); print DB @gunlog; close(DB);
            $log = ($log . "���Ƥ��ä������ब����Ƥ��ޤä���<BR><br>���������������������ؤ���ٹ𲻤�����������<BR><BR><font color=\"red\">����������������<br><br><b>$f_name $l_name��$cl $sex$no�֡ˤϻ�˴������</b></font><br>") ;
        }
    }else{
        $itai[$paso] --;
        if ($itai[$paso] == 0) {
            $log = ($log . "��Х���PC �ΥХåƥ�����Ϥ�Ȥ��̤�������<BR>") ;
        }
    }

    &SAVE;
}
1
