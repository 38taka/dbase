#!/usr/bin/env perl
use strict;
use warnings;
use CGI qw(:standard);

# データファイルを読み込み
my $data_file = 'data.dat';
open my $fh, '<', $data_file or die "Could not open '$data_file': $!";
my @users = <$fh>;
close $fh;

# クエリを取得
my $query = param('query');

# ユーザー情報を検索
my $result;
foreach my $user (@users) {
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
print header;
print start_html('ユーザー情報検索結果');
if ($result) {
    print h1("検索結果"),
          p("名前: $result->{name}"),
          p("ID: $result->{id}"),
          p("アカウント: $result->{account}"),
          p("メールアドレス: $result->{email}"),
          p("パスワード: $result->{password}");
} else {
    print h1("該当するユーザーが見つかりません");
}
print end_html;
