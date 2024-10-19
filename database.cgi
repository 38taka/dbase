#!/usr/bin/perl
use strict;
use warnings;
use CGI qw(:standard);
use Encode;

# �f�[�^�t�@�C����ǂݍ���
my $data_file = 'data.dat'; # XAMPP�Ŏg���ꍇ�̃p�X
open my $fh, '<:encoding(shiftjis)', $data_file or die "Could not open '$data_file': $!";
my @users = <$fh>;
close $fh;

# �N�G�����擾
my $query = decode('shiftjis', param('query'));

# ���[�U�[��������
my $result;
foreach my $user (@users) {
    chomp $user;
    my ($name, $id, $account, $email, $password) = split /,/, $user;
    if ($id eq $query || $account eq $query || $email eq $query) {
        $result = {
            name => $name,
            id => $id,
            account => $account,
            email => $email,
            password => $password,
        };
        last;
    }
}

# HTML�o��
print header(-charset => 'Shift_JIS');
print start_html(-title => '���[�U�[��񌟍�����', -encoding => 'Shift_JIS');
if ($result) {
    print h1("��������"),
          p("���O: " . encode('shiftjis', $result->{name})),
          p("ID: " . encode('shiftjis', $result->{id})),
          p("�A�J�E���g: " . encode('shiftjis', $result->{account})),
          p("���[���A�h���X: " . encode('shiftjis', $result->{email})),
          p("�p�X���[�h: " . encode('shiftjis', $result->{password}));
} else {
    print h1("�Y�����郆�[�U�[��������܂���");
}
print end_html;
