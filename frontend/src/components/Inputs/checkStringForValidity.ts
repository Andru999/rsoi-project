export const checkStringForValidity = (str: string, alphabet: string) => {
		str = str.trim();
		if (!str) {
			return "";
		}
		
		for (let i = 0; i < str.length; i++) {
			if (!alphabet.includes(str[i])) {
				str = str.replace(str[i], "");
				break;
			}
		}

		return str;
};
