#!/usr/bin/perl

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
    my ($id, $seibetu,$inumber, $email, $benes) = split /,/, $user;
    if ($id eq $query || $account eq $query || $email eq $query) {
        $result = {
            id => $id,
            seibetu => $seibetu
            inumber => $inumber,
            hnumber => $hnumber
            email => $email,
            benes => $benes,
        };
        last;
    }
}

# HTML出力
print header;
print start_html('ユーザー情報検索結果');
if ($result) {
    print h1("検索結果"),
          p("学籍番号: $result->{id}"),
          p("性別: $result->{seibetu}"),
          p("端末番号: $result->{inumber}"),
          p("電話番号: $result->{hnumber}"),
          p("メールアドレス: $result->{email}"),
          p("Benesse ID: $result->{benes}");
} else {
    print h1("該当するユーザーが見つかりません");
}
print end_html;
