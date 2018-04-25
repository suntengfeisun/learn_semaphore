# learn_semaphore
学习使用python的semaphore <br>
以前使用threading的时候使用类似print的输出，会输出如下类似的乱序 <br>
```python
('thread_6', 56)
('thread_5', 57)
('thread_5', 61)
('thread_5', 62)
('thread_0', 45)
('thread_0', 64)
(('thread_3''th, re47ad)_2
', 48)
('thread_3', 66)
('thread_3', 68)
(('t'ht(rher'aetdah_dr9_e'7a'd, _, 452'55) )
('
th, read_8'54)
, 58)('thread_6', (('th
re60a'dt_h1r'ea, d_5', 63)
59)
)
('thread_9', 70)
('thread_4', 72)

```
这是因为thread之间争夺print的原因 <br>
现在我尝试引入Semaphore就解决了这个问题
```python
('thread_0', 0)
('thread_1', 1)
('thread_3', 3)
('thread_4', 4)
('thread_0', 5)
('thread_3', 8)
('thread_3', 12)

```