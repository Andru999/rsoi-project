import "./Texts.css";


interface TextErrorPageProps {
	header: string,
	text: string,
	openMiniDrawer: boolean,
}

export function TextErrorPage({ header, text, openMiniDrawer }: TextErrorPageProps) {
	return (
		<div className={`${openMiniDrawer ? "short-text-error-page-container" : "long-text-error-page-container"}`}>
			<p className="text-error-page-header">
				{ header }
			</p>
			<p className="text-error-page">
				{ text }
			</p>
		</div>
	)
}
