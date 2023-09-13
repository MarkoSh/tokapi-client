from client.api import TokApi
from examples.constants import API_KEY, BASE_URL


def example(video_id: str):
    """
    Print video comments
    """
    api = TokApi(API_KEY, BASE_URL)

    offset = 0
    for i in range(0, 3):
        result = api.get_video_comments(video_id, count=2, offset=offset)
        data = result.json()

        for comment in data['comments']:
            print('ID: {}, text: {}'.format(comment['cid'], comment['text']))

        offset = data['cursor']


if __name__ == "__main__":
    example('6977747303692078337')
