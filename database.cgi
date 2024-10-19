#!/usr/bin/perl
use strict;
use warnings;
use CGI qw(:standard);
use Encode;

# データファイルを読み込み
my $data_file = 'data.dat'; # XAMPPで使う場合のパス
open my $fh, '<:encoding(shiftjis)', $data_file or die "Could not open '$data_file': $!";
my @users = <$fh>;
close $fh;

# クエリを取得
my $query = decode('shiftjis', param('query'));

# ユーザー情報を検索
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

# HTML出力
print header(-charset => 'Shift_JIS');
print start_html(-title => 'ユーザー情報検索結果', -encoding => 'Shift_JIS');
if ($result) {
    print h1("検索結果"),
          p("名前: " . encode('shiftjis', $result->{name})),
          p("ID: " . encode('shiftjis', $result->{id})),
          p("アカウント: " . encode('shiftjis', $result->{account})),
          p("メールアドレス: " . encode('shiftjis', $result->{email})),
          p("パスワード: " . encode('shiftjis', $result->{password}));
} else {
    print h1("該当するユーザーが見つかりません");
}
print end_html;
