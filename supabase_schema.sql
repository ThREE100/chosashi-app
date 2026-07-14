-- 土地家屋調査士トレーニングアプリ: Supabaseスキーマ再構築
-- Supabase Dashboard > SQL Editor にそのまま貼り付けて実行してください

-- 択一/暗記の正誤記録
create table if not exists progress (
  user_id uuid not null references auth.users(id) on delete cascade,
  question_id text not null,
  correct int not null default 0,
  wrong int not null default 0,
  last_result text not null,
  updated_at timestamptz not null default now(),
  primary key (user_id, question_id)
);

-- 間隔反復(SM-2簡易版)スケジュール
create table if not exists srs (
  user_id uuid not null references auth.users(id) on delete cascade,
  question_id text not null,
  ease numeric not null,
  ivl int not null,
  reps int not null,
  due text not null,
  updated_at timestamptz not null default now(),
  primary key (user_id, question_id)
);

-- 学習記録(日次の時間・回答数)
create table if not exists studylog (
  user_id uuid not null references auth.users(id) on delete cascade,
  day text not null,
  min int not null default 0,
  ans int not null default 0,
  correct int not null default 0,
  updated_at timestamptz not null default now(),
  primary key (user_id, day)
);

-- RLS: 本人の行だけ読み書き可能にする
alter table progress enable row level security;
alter table srs enable row level security;
alter table studylog enable row level security;

create policy "own progress" on progress for all
  using (auth.uid() = user_id) with check (auth.uid() = user_id);
create policy "own srs" on srs for all
  using (auth.uid() = user_id) with check (auth.uid() = user_id);
create policy "own studylog" on studylog for all
  using (auth.uid() = user_id) with check (auth.uid() = user_id);
