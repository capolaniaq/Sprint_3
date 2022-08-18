const btn_insert_room = document.getElementById('insert_room');

btn_insert_room.addEventListener('click', () => {

	const table_room = document.getElementById('table_rooms');

	table_room.style.cssText = 'display: none';
	btn_insert_room.style.cssText = 'display: none';

	const form_insert = document.getElementById('div_insert');
	form_insert.style.cssText = 'display: block';

	btn_cancel_room.style.cssText = 'display: block';

})

const btn_cancel_room = document.getElementById('cancel_insert');

btn_cancel_room.addEventListener('click', () =>{

	btn_cancel_room.style.cssText = 'display: none';

	const table_room = document.getElementById('table_rooms');
	table_room.style.cssText = 'display: block';

	const form_insert = document.getElementById('div_insert');
	form_insert.style.cssText = 'display: none';

	btn_insert_room.style.cssText = 'display: block';
})


const btn_delete = document.getElementById('delete');

btn_delete.addEventListener('click', () =>{
	
})