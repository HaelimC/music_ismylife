# Generated by Django 5.1.3 on 2024-11-26 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DailyPlaylists',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('playlist_title', models.CharField(max_length=252, verbose_name='Playlist Title')),
                ('playlist_url', models.URLField(max_length=255, verbose_name='Playlist URL')),
                ('thumbnail', models.URLField(blank=True, max_length=255, null=True, verbose_name='Thumbnail')),
                ('platform', models.CharField(choices=[('youtube', 'YouTube'), ('spotify', 'Spotify')], max_length=10, verbose_name='Platform')),
            ],
            options={
                'verbose_name': 'Daily Playlist',
                'verbose_name_plural': 'Daily Playlists',
                'db_table': 'daily_playlists',
            },
        ),
        migrations.CreateModel(
            name='DailySongs',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('song_title', models.CharField(max_length=255, verbose_name='Song Title')),
                ('song_url', models.URLField(max_length=255, verbose_name='Song URL')),
                ('thumbnail', models.URLField(blank=True, max_length=255, null=True, verbose_name='Thumbnail')),
                ('platform', models.CharField(choices=[('youtube', 'YouTube'), ('spotify', 'Spotify')], max_length=10, verbose_name='Platform')),
            ],
            options={
                'verbose_name': 'Daily Song',
                'verbose_name_plural': 'Daily Songs',
                'db_table': 'daily_songs',
            },
        ),
        migrations.CreateModel(
            name='SearchPlaylist',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('playlist_title', models.CharField(max_length=252, verbose_name='Playlist Title')),
                ('playlist_url', models.URLField(max_length=255, verbose_name='Playlist URL')),
                ('thumbnail', models.URLField(blank=True, max_length=255, null=True, verbose_name='Thumbnail')),
                ('platform', models.CharField(choices=[('youtube', 'YouTube'), ('spotify', 'Spotify')], max_length=10, verbose_name='Platform')),
            ],
            options={
                'verbose_name': 'Search Playlist',
                'verbose_name_plural': 'Search Playlists',
                'db_table': 'search_playlist',
            },
        ),
        migrations.CreateModel(
            name='SearchSongs',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('song_title', models.CharField(max_length=255, verbose_name='Song Title')),
                ('song_url', models.URLField(max_length=255, verbose_name='Song URL')),
                ('thumbnail', models.URLField(blank=True, max_length=255, null=True, verbose_name='Thumbnail')),
                ('platform', models.CharField(choices=[('youtube', 'YouTube'), ('spotify', 'Spotify')], max_length=10, verbose_name='Platform')),
            ],
            options={
                'verbose_name': 'Search Song',
                'verbose_name_plural': 'Search Songs',
                'db_table': 'search_songs',
            },
        ),
    ]
