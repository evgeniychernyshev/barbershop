INSERT INTO t_barbers (id, name, level, img_path, is_working) VALUES
('2288262b-0700-4a7f-88e8-9fae65f01cb7', 'Сергей', 'Junior', 'static/sergey.jpg', 1),
('8c1e3beb-cef2-47e3-853f-0b7a9bd748d7', 'Михаил', 'Senior', 'static/michael.jpg', 1);

INSERT INTO t_timetable (id, time, barber_id) VALUES
('ac34f730-f63b-4222-9851-946c90b8edb0', 10, '2288262b-0700-4a7f-88e8-9fae65f01cb7'),
('07afd0ed-847b-4d4d-b634-fb61610d0403', 11, '2288262b-0700-4a7f-88e8-9fae65f01cb7'),
('3ab6014b-4836-4d91-85ef-93d32859924f', 12, '2288262b-0700-4a7f-88e8-9fae65f01cb7'),
('b49e90a0-48c4-4c66-b623-173356136746', 13, '2288262b-0700-4a7f-88e8-9fae65f01cb7'),
('51154a88-fd28-4a06-b5c5-80fe9160e614', 14, '2288262b-0700-4a7f-88e8-9fae65f01cb7'),
('ddedc31b-d501-42e4-9bf3-94ad817ad226', 15, '2288262b-0700-4a7f-88e8-9fae65f01cb7'),
('b3286bee-6475-4e1c-99d2-a70c510f6f0f', 16, '2288262b-0700-4a7f-88e8-9fae65f01cb7'),
('295e8f4a-a97e-44c9-9541-eaa3a60938e0', 17, '2288262b-0700-4a7f-88e8-9fae65f01cb7'),
('cb96f2b0-8566-4325-a2ee-66bc7b570d33', 18, '2288262b-0700-4a7f-88e8-9fae65f01cb7'),
('70874898-b7a0-4142-98ad-b7d27fb245e3', 10, '8c1e3beb-cef2-47e3-853f-0b7a9bd748d7'),
('29b774ce-0aa7-45fa-b235-323f3a9786ee', 11, '8c1e3beb-cef2-47e3-853f-0b7a9bd748d7'),
('67669294-9872-4df3-ac7d-794509382109', 12, '8c1e3beb-cef2-47e3-853f-0b7a9bd748d7'),
('3824b4dd-7205-4a48-a680-6ee534b24991', 13, '8c1e3beb-cef2-47e3-853f-0b7a9bd748d7'),
('a8217c4a-b5ad-4328-89b6-5173dbe2f342', 14, '8c1e3beb-cef2-47e3-853f-0b7a9bd748d7'),
('0b171216-10c3-45f4-bb2a-09eb6c54196d', 15, '8c1e3beb-cef2-47e3-853f-0b7a9bd748d7'),
('0b3e7384-34b4-457c-9741-c875a0766e1f', 16, '8c1e3beb-cef2-47e3-853f-0b7a9bd748d7'),
('d2373a63-e4a4-4299-8ce4-fa7126c491c3', 17, '8c1e3beb-cef2-47e3-853f-0b7a9bd748d7'),
('4fc86b19-5ea6-4fc6-be84-c69297dce622', 18, '8c1e3beb-cef2-47e3-853f-0b7a9bd748d7');

INSERT INTO t_service (id, name, price, level) VALUES
('4857fe41-76c9-4236-b20c-247d4f1f1668', 'Стрижка', 800, 'Junior'),
('d8ef92e9-e1b9-4e8b-99a6-3dfc2b08ef21', 'Стрижка', 1000, 'Senior'),
('3694018f-dc68-41cd-9dc9-aeb8bff5df2f', 'Стрижка', 1400, 'Lead');

INSERT INTO t_clients (id, name, phone, time_id, barber_id) VALUES
('515e28c9-2868-4043-8495-aef53f52e621', 'Андрей', '79000000000', '3ab6014b-4836-4d91-85ef-93d32859924f', '8c1e3beb-cef2-47e3-853f-0b7a9bd748d7'),
('cc35815f-a251-4f04-81b3-df883369cd45', 'Георгий', '79111111111', 'b49e90a0-48c4-4c66-b623-173356136746', '8c1e3beb-cef2-47e3-853f-0b7a9bd748d7');