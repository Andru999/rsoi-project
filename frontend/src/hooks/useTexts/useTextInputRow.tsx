import { useState } from 'react';


export function useTextInputRow() {
	const [hint, setHint] = useState("");

	return { 
		hint, 
		setHint
	};
};
