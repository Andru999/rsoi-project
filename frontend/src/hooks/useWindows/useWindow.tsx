import { useState } from 'react';


export function useWindow() {
	const [visibility, setVisibility] = useState(false);

	const handleOpenWindow = () => {
		setVisibility(true);
	};

	const handleCloseWindow = () => {
		setVisibility(false);
	};

	return { visibility, handleOpenWindow, handleCloseWindow };
};
