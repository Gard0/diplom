from sender_stand_request import post_new_order, get_order_info


# Получение трека заказа:
def get_track_number():
    track = post_new_order().json()["track"]
    return track


# ТЕСТ:
# 1. Выполнить запрос на создание заказа.
# 2. Сохранить номер трека заказа.
# 3. Выполнить запрос на получения заказа по треку заказа.
# 4. Проверить, что код ответа равен 200.
def test_create_and_track_order():
    track = get_track_number()
    get_response = get_order_info(track)
    assert get_response.status_code == 200
