#==================#
# �� Ϣ³��ƶػ�  #
#==================#

    local($iplog) = "$ADM_DIR/post.log";  # ��Ͽ�ǡ����ե�����̾

    open(IN,"$iplog"); @data = <IN>; close(IN);

    @new=();
    $flag=0;
    foreach (@data) {
        ($w_now,$w_host) = split(/<>/);

        if (($now - 60) > $w_now) { next; }
        elsif ($w_host eq $host) {
            if (($w_now + $lim_sec) > $now) { &ERROR("Ϣ³������¤򤷤Ƥ��ޤ����⤦������ä����ư���Ƥ���������"); }
            $_ = "$now<>$host<>\n";
            $flag=1;
        }
        push(@new,$_);
    }

    if (!$flag) {
        push(@new,"$now<>$host<>\n");
    }
    $playmem = @new;

    open(OUT,">$iplog"); seek(OUT,0,0); print OUT @new; close(OUT);

1
