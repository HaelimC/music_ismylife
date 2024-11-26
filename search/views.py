from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import DailySongs, DailyPlaylists, SearchSongs, SearchPlaylist
import time

def index(request):
    daily_songs = DailySongs.objects.all()
    daily_playlists = DailyPlaylists.objects.all()[:10]

    print(f"Daily Songs count: {daily_songs.count()}")
    print(f"Daily Playlists count: {daily_playlists.count()}")

    for song in daily_songs:
        print(f"Song: {song.song_title}, URL: {song.song_url}")

    for playlist in daily_playlists:
        print(f"Playlist: {playlist.playlist_title}, URL: {playlist.playlist_url}")

    context = {
        'daily_songs': daily_songs,
        'daily_playlists': daily_playlists,
    }
    return render(request, 'search/index.html', context)


import requests
from requests.auth import HTTPBasicAuth

@csrf_exempt
def trigger_airflow_dag(request):
    if request.method == "POST":
        input_value = request.POST.get("input_value")
        platform = request.POST.get("platform")

        if not input_value:
            return JsonResponse({"error": "검색어를 입력해주세요!"}, status=400)
        
        if not platform:
            return JsonResponse({"error": "검색 플랫폼을 선택해주세요!"}, status=400)

        # 세션에 저장
        request.session['platform'] = platform
        request.session['input_value'] = input_value

        airflow_url = "http://airflow_007-airflow-webserver:8080/api/v1/dags/etl_dag_search_songs/dagRuns"
        airflow_url_playlist = "http://airflow_007-airflow-webserver:8080/api/v1/dags/etl_dag_playlist/dagRuns"
        username = 'airflow'
        password = 'airflow'

        payload = {
            "conf": {"input_value": input_value}
        }

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }

        try:
            response = requests.post(airflow_url, json=payload, headers=headers, auth=HTTPBasicAuth(username, password))
            response_play = requests.post(airflow_url_playlist, json=payload, headers=headers, auth=HTTPBasicAuth(username, password))
            if response.status_code == 200 and response_play.status_code == 200:
                time.sleep(5)
                # 트리거 성공 후 결과 페이지로 리디렉션
                return redirect('result')  # 'result'는 결과 페이지의 URL 이름
            else:
                return JsonResponse({"error": response.json()}, status=response.status_code)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=405)



def result(request):    
    # 세션에서 정보 가져오기
    platform = request.session.get('platform', None)
    input_value = request.session.get('input_value', None)

    # 모든 데이터 가져오기
    search_songs = SearchSongs.objects.all()
    search_playlists = SearchPlaylist.objects.all() 

    # 템플릿으로 데이터 전달
    context = {
        'search_songs': search_songs,
        'search_playlists': search_playlists,
        'platform': platform,  # 플랫폼 정보 전달
        'input_value': input_value,
    }
    return render(request, 'search/result.html', context)
