#!/usr/bin/perl -w
use strict;
use warnings;

my $smtp_client_count = 5;

#
# Initalize and open syslog.
#
#openlog('postfix/randomizer','pid','mail');
#
# Autoflush standard output.
#
select STDOUT; $|++;

while (<>) {
    chomp;
    my $random_smtp_index = int(rand($smtp_client_count)) + 1;
    if (/^get\s(.+)$/i) {
        print "200 smtp$random_smtp_index\n";
        #syslog("info","Using: %s Transport Service", $random_smtp);
        next;
    }
    print "200 smtp:\n";
}

