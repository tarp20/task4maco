import math


def pack_up(order):
    try:
        order = int(str(order))
    except ValueError:
        return "C'mon, enter int number"
    box = [0, 0, 0]
    if 0 < order < 101:
        if order < 18:
            box[2] = box[2]+order//18*2
            rest = order % 18
        else:
            box[2] = box[2]+order//9
            rest = order % 9
        qty_box = [math.ceil(rest/3), math.ceil(rest/6), math.ceil(rest/9)]
        min_qty_box = min(qty_box)
        index_min_qty_box = qty_box.index(min_qty_box)
        free_place = [(min_qty_box*3-rest), (min_qty_box*6-rest),
                      (min_qty_box*9-rest)]
        min_free_place = min(free_place[index_min_qty_box:])
        box[free_place.index(min_free_place)] += min_qty_box
        answer = box
        if sum(box) > 1:
            answer.append(math.ceil(sum(box)/3))
        else:
            answer.append(0)
        answer.insert(0, order)

    elif order > 100:
        return 'We are not Amazon and do not serve large orders'
    else:
        return 'Are you serious? Enter positive value'

    print(f'For order {answer[0]} pieces need to use {answer[1]} small box(es),\
        {answer[2]} medium box(es), {answer[3]} big box(es) \
        and pack those boxes in {answer[4]} box(es).')

    return answer


print(pack_up(14))


def test_answer():
    assert pack_up(3) == [3, 1, 0, 0, 0]
    assert pack_up(19) == [19, 1, 0, 2, 1]
    assert pack_up(11) == [11, 0, 2, 0, 1]
    assert pack_up(14) == [14, 0, 0, 2, 1]
    assert pack_up(24) == [24, 0, 1, 2, 1]
    assert pack_up(33) == [33, 0, 1, 3, 2]
    assert pack_up(1000) == 'We are not Amazon and do not serve large orders'
    assert pack_up(-30) == 'Are you serious? Enter positive value'
    assert pack_up('abc') == "C'mon, enter int number"
    assert pack_up(1.5) == "C'mon, enter int number"
