import { useState } from 'react';


export function useDropdownList() {
	const [open, setOpen] = useState(false);

	const handleClick = () => {
		setOpen(!open);
	};

	const handleOpen = () => {
		setOpen(true);
	};

	const handleClose = () => {
		setOpen(false);
	};

	return { open, handleClick, handleOpen, handleClose };
};
