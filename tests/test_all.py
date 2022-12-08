# Validate that I haven't broken any of my previous solutions
import pytest
import subprocess

# This file shouldn't exist on remote,
# So if you cloned this for some reason it'll fail.
with open('tests/key.txt') as f:
    key = {}
    l = f.readlines()
    for i in range(len(l)):
        key[f'day{i+1}'] = tuple(l[i].strip().split())


@pytest.mark.parametrize("day", key)
@pytest.mark.parametrize("style", ["normal", "golf"])
def test_solution(day, style):
    if style == "normal":
        for j in range(2):
            result = subprocess.run(
                ['python', f'{day}{"part2"*j}.py'],
                cwd=f'{day}/', text=True, capture_output=True
            )
            assert result.stderr == ''
            assert result.stdout.strip() == key[day][j]
    elif style == 'golf':
        # I'll need to fix this if I start separating the golfs by part again.
        result = subprocess.run(
            ['python', f'{day}golf.py'],
            cwd=f'{day}/', text=True, capture_output=True
        )
        assert result.stderr == ''
        assert tuple(map(str.strip, result.stdout.split())) == key[day]
